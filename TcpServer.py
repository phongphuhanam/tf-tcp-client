import socketserver
import threading
import logging, os, time
from TCPserver import tf_ns_msg_pb2

# lock_rd = threading.Lock()


class MyTCPHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        print(server.lock_rd)

    def setup(self):
        super().setup()

    def readVarintPrefix(self):
        count = 0

        current_byte = ord(self.request.recv(1))
        # print(current_byte)
        if not current_byte:
            return -2

        return_value = current_byte & 0x7f
        count = count + 1
        while (current_byte & 0x80) :
            current_byte = ord(self.request.recv(1))
            # print(current_byte)
            count = count + 1
            if not current_byte or count > 4:
                return -1
            return_value |= (current_byte & 0x7F) << (7 * (count - 1)) # Add the next 7 bits
        return return_value


    def writeVarintPrefix(self, value):
        data = []
        bits = value & 0x7f
        value >>= 7
        while value:
            conv_data = 0x80 | bits
            data.append(chr(conv_data & 0xff))
            bits = value & 0x7f
            value >>= 7
        data.append(chr(bits & 0xff))
        msg = "".join(data)
        encoded_msg = str.encode(msg, encoding="latin1")
        return encoded_msg

    def handle(self):
        # self.request is the TCP socket connected to the client
        current_thread_status = "{}:{}:".format(self.client_address[0], self.client_address[1])
        connected = True
        connection_established = False
        car_id = 0

        input_list_index = -1
        output_list_index = -1

        while connected:
            msg_length = self.readVarintPrefix()

            if msg_length == -2:
                continue

            if msg_length > 0:
                tfcommand = tf_ns_msg_pb2.Command()
                self.data = self.request.recv(msg_length)
                try:
                    tfcommand.ParseFromString(self.data)
                    # print(tfcommand.command_type)
                    if tfcommand.command_type == 1:
                        car_id = tfcommand.carid
                        connected = False
                    elif tfcommand.command_type == 4:
                        car_id = tfcommand.carid
                        print(current_thread_status + "Connection established: {} - wait for command".format(car_id))
                        self.server.lock_vehicle_list.acquire()
                        self.server.carid_list.append(car_id)
                        self.server.lock_vehicle_list.release()

                        connection_established = True
                    # vehicle received feature payload from other car
                    elif tfcommand.command_type == 2:
                        # car_id = tfcommand.carid
                        msg_length = self.readVarintPrefix()
                        if msg_length > 0:
                            print(current_thread_status + "{}: {} -> {}".format(tfcommand.simulattionTime,
                                                                                tfcommand.carid, car_id))

                            print(self.server.lock_rd)
                            print(threading.current_thread())

                            self.server.lock_rd.acquire()
                            weigh_data = self.request.recv(msg_length)
                            tfweights = tf_ns_msg_pb2.WeightArray()
                            tfweights.ParseFromString(weigh_data)
                            # print(current_thread_status + "Weight info.: {} length: {}".format(tfweights.carid, tfweights.lenght))
                            self.server.output_tf_data.append(tfweights)
                            self.server.lock_rd.release()

                            # for tf_element in server.ns_data_queue:
                            #     if tf_element.carid == tfweights.carid:
                            #         for i in range(0, tfweights.lenght):
                            #             tf_element.weights[i] = tfweights.weights[i]
                            # else:
                            #     server.ns_data_queue.append(tfweights)

                            # for i in range(0, tfweights.lenght):
                            #     print("{} : {} ".format(i, tfweights.weights[i],), end="", flush=True)
                            #     # if i % 10 == 0:
                            #     #     print("  ")
                            # print("")

                    elif tfcommand.command_type == 3:
                        # OK now if there is data want to send from Tensorflow start sending
                        # car_id = tfcommand.carid
                        weight_size = tfcommand.weightLen
                        print(current_thread_status + "{} payload length: {} vehicle: {}".format(tfcommand.simulattionTime, weight_size, car_id))
                        send_done = False

                        # wait here until get data from main thread
                        while not send_done:
                            with self.server.lock_wr:
                                for tfw_ele in self.server.input_tf_data:
                                    if tfw_ele.carid == car_id:
                                        tf_weights_response = tfw_ele
                                        weight_payload = tf_weights_response.SerializeToString()
                                        # print(tf_weights_response.ByteSize())
                                        # print(len(weight_payload))
                                        self.request.sendall(self.writeVarintPrefix(tf_weights_response.ByteSize())
                                                             + weight_payload)
                                        print(current_thread_status + "sending done")
                                        send_done = True

                                    if send_done:
                                       break
                                # else:
                                #     print("Empty list: No data was sent")

                except Exception as e:
                    print(e)

        # finish transmission clear list index
        print(current_thread_status + "Connection finished: {}".format(car_id))
        self.server.lock_vehicle_list.acquire()
        self.server.carid_list.pop(self.server.carid_list.index(car_id))
        self.server.lock_vehicle_list.release()



if __name__ == "__main__":
    HOST, PORT = "", 26789
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.lock_rd = threading.RLock()
    server.lock_wr = threading.RLock()
    server.lock_vehicle_list = threading.RLock()
    server.carid_list = []
    server.input_tf_data = []
    server.output_tf_data = []

    print("Server establised")
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    # ()
    # server.handle_request()

    print("process ID: ", os.getpid())


    # for i in server.carid_lis
    #
    # for index in server.tf_data_queue:
    #     index.lenght = 256
    #     index.weights.clear()
    #     for i in range(0, index.lenght):
    #         index.weights.append(i + 3.1412568)
    # server.lock_wr.release()

    while True:
        # server.lock_wr.acquire()
        with server.lock_vehicle_list:
            if len(server.carid_list) > 0:
                # print(len(server.carid_list))
                server.lock_wr.acquire()
                server.input_tf_data.clear()
                for carid in server.carid_list:
                    tfdat = tf_ns_msg_pb2.WeightArray()
                    tfdat.carid = carid
                    tfdat.lenght = 256
                    for i in range(0, tfdat.lenght):
                        tfdat.weights.append(i + 3.1412568)
                    server.input_tf_data.append(tfdat)

                server.lock_wr.release()

        with server.lock_rd:
            for tf_index in server.output_tf_data:
                print("Weight info.: {} length: {}".format(tf_index.carid, tf_index.lenght))
            server.output_tf_data.clear()


