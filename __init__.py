import os

# def readVarintPrefix():
#     count = 0
#
#     current_byte = ord(self.request.recv(1))
#     # print(current_byte)
#     if not current_byte:
#         return -2
#
#     return_value = current_byte & 0x7f
#     count = count + 1
#     while (current_byte & 0x80):
#         current_byte = ord(self.request.recv(1))
#         # print(current_byte)
#         count = count + 1
#         if not current_byte or count > 4:
#             return -1
#         return_value |= (current_byte & 0x7F) << (7 * (count - 1))  # Add the next 7 bits
#     return return_value


def writeVarintPrefix(value):
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
