import struct
import zlib
# Constants
KEY = '470FC614'
def task_func(hex_string=KEY):
    binary_float = struct.pack('!f', int(hex_string, 16))
    compressed_data = zlib.compress(binary_float)
    return compressed_data