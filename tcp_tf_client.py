import socket
import time
from tftcpClient import tf_ns_msg_pb2
from tftcpClient import *

HOST, PORT = "", 26789


class TCPClient:

    def __init__(self, carid, host="pplabpc.iptime.org", port=26789):
        self.host = host
        self.port = port
        self.carid = carid
        self.client = None
        self.is_received_payload = False
        self.cmd = tf_ns_msg_pb2.Command()
        self.cmd.carid = carid
        self.cmd.platform_type = 1

    def request_payload(self, carid):
        self.carid = carid
        self.cmd.carid = carid
        self.cmd.simulattionTime = 1
        print("Request vehicle_id: {}".format(self.carid))
        self.connect()
        recv_payload = self.recv_weights()
        self.close()
        print("Request success")
        return recv_payload

    def send_payload(self, carid, payload):
        self.carid = carid
        self.cmd.carid = carid
        self.cmd.simulattionTime = 1
        print("Send vehicle_id: {}".format(self.carid))
        self.connect()
        self.send_weights(payload)
        self.close()
        print("Send success")

    def request_finish(self, carid):
        self.carid = carid
        self.cmd.carid = carid
        self.cmd.simulattionTime = 1
        print("Send vehicle_id: {}".format(self.carid))
        self.connect()
        self.send_finish()
        self.close()
        print("Send success")

    def request_vehicle_list(self):
        self.connect()
        self.cmd.command_type = 6
        res = self._recv_payload()
        self.close()
        res_list = []
        for i in range(res.total_object):
            res_list.append(res.payload[i].object_id)
        return res_list

    # def request_valid_payload(self, carid):

    def readVarintPrefix(self):
        count = 0

        current_byte = ord(self.client.recv(1))
        # print(current_byte)
        if not current_byte:
            return -2

        return_value = current_byte & 0x7f
        count = count + 1
        while (current_byte & 0x80) :
            current_byte = ord(self.client.recv(1))
            # print(current_byte)
            count = count + 1
            if not current_byte or count > 4:
                return -1
            return_value |= (current_byte & 0x7F) << (7 * (count - 1)) # Add the next 7 bits
        return return_value

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def _recvBuffer(self, length):
        weigh_data = b''
        while length > 0:
            segment_payload = self.client.recv(length)
            if segment_payload:
                current_recv_size = len(segment_payload)
                # print("expected: {} received {}".format(length, current_recv_size))
                length = length - current_recv_size
                weigh_data += segment_payload

        return weigh_data

    def send_weights(self, payload):
        self.cmd.command_type = 2
        size_msg = writeVarintPrefix(self.cmd.ByteSize())
        self.client.sendall(size_msg + self.cmd.SerializeToString())

        payload.carid = self.carid
        size_wg = writeVarintPrefix(payload.ByteSize())
        self.client.sendall(size_wg + payload.SerializeToString())

    def clear_all_queue(self):
        self.cmd.command_type = 5
        size_msg = writeVarintPrefix(self.cmd.ByteSize())
        self.client.sendall(size_msg + self.cmd.SerializeToString())

    def recv_weights(self):
        self.cmd.command_type = 3
        return self._recv_payload()

    def _recv_payload(self):
        size_msg = writeVarintPrefix(self.cmd.ByteSize())
        total_sending_byte = len(size_msg) + self.cmd.ByteSize()
        self.client.sendall(size_msg + self.cmd.SerializeToString())
        # while sendbytes != total_sending_byte:
        #     time.sleep(0.1)
        #     sendbytes = self.client.send(size_msg + self.cmd.SerializeToString())

        recvbytes = -1
        while recvbytes < 0:
            recvbytes = self.readVarintPrefix()
        # print(recvbytes)

        if recvbytes > 0:
            weigh_data = self._recvBuffer(recvbytes)
            tfweights = tf_ns_msg_pb2.WeightArray()
            tfweights.ParseFromString(weigh_data)
            print("Weight info: vehicle ID {} : size {}".format(tfweights.carid, tfweights.ByteSize()))
            return tfweights
        else:
            return None

    def send_finish(self):
        finish_weight_data = tf_ns_msg_pb2.WeightArray()
        finish_weight_data.msg_status = finish_weight_data.FINISH
        finish_weight_data.simulationTime = 15
        self.send_weights(finish_weight_data)


    def close(self):
        self.cmd.command_type = 1
        size_msg = writeVarintPrefix(self.cmd.ByteSize())
        self.client.sendall(size_msg + self.cmd.SerializeToString())

        self.client.close()


if __name__ == "__main__":

    send_weights_data = tf_ns_msg_pb2.WeightArray()
    send_weights_data.request_type = 1
    for index in range(0, 5):
        object1_data = send_weights_data.payload.add()
        object1_data.object_id = 1
        object1_data.length = 256
        for i in range(0, object1_data.length):
            object1_data.weights.append(i + 3.1412568)
        object1_data.angle = 90.06

    tfclient = TCPClient(0)

    # tfclient.connect()
    # print("Connect success")
    # tfclient.clear_all_queue()
    # print("Clear queue success")
    # tfclient.close()

    timeout_cnt = 0

    for dat in range(0, 171):
        vehicle_list = tfclient.request_vehicle_list()

        for i in vehicle_list:
            tfclient.send_payload(carid=i, payload=send_weights_data)
        time.sleep(0.2)

        # total_success_node = [0]
        success_flag_list = []
        for i in vehicle_list:
            success_flag_list.append(0)
        total_success = 0
        veh_index = 0
        total_vehs = len(vehicle_list)
        while total_success < total_vehs:
            if success_flag_list[veh_index] == 0:
                tfclient.cmd.request_type = 1
                res_payload = tfclient.request_payload(carid=vehicle_list[veh_index])
                if res_payload.msg_status == 1:
                    # ns simulation done, we should finish
                    print("ns simulation finish")
                elif res_payload.msg_status == 2:
                    timeout_cnt += 1
                    time.sleep(0.1)
                    if timeout_cnt % 10 == 0:
                        print("TIME OUT on node {}".format(vehicle_list[veh_index]))
                elif res_payload.msg_status == 0:

                    success_flag_list[veh_index] = 1
                    total_success += 1
                    # recv_data_queue.append(res_payload)
                    print("successfully receive data sended_id {}".format(res_payload.sended_id))
                    compare_payload = tf_ns_msg_pb2.WeightArray()
                    compare_payload.carid = vehicle_list[veh_index]
                    compare_payload.total_object = 3
                    compare_payload.request_type = 2
                    for j in range(compare_payload.total_object):
                        obj = compare_payload.payload.add()
                        obj.comparison_object_id = 2

                    compare_payload.simulationTime = 15
                    tfclient.send_payload(carid=vehicle_list[veh_index], payload=compare_payload)

            veh_index = veh_index + 1
            veh_index = veh_index % total_vehs

        # recv_data_queue

    for i in range (0, 2):
        tfclient.request_finish(i)