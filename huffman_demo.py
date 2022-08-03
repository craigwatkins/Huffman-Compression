# -*- coding: utf-8 -*-
"""
Demonstration of how to use huffman_canonical

"""


import padded_binary as pb
from huffman_compression import HuffmanCoding


with open('dorianGrayCh1.txt', 'r', encoding="utf8") as file_obj:
    text = file_obj.read()
data = [ord(char) for char in text]
huff = HuffmanCoding()
save_info, encoded_list = huff.compress(data)
pb.write_padded_bytes(save_info, 'huffman.bin')
binaries = pb.read_padded_bytes('huffman.bin')
decompressed = huff.decompress_file(binaries)
if data == decompressed:
    print('huffman successful!')
else:
    print('huffman failed!')
    print('data: ', data[0:10])
    print('uncompressed: ', decompressed[0:10])
