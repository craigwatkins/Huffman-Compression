# Huffman-Compression
Python implementation of Huffman compression using canonical codes

I created this code because I wanted an implementation of the Huffman algorithm that I couldn't find in python. It uses canonical code and saves the Huffman code dictionary with a combination of sorted symbols and the number of bits for each symbol. This is ideal for situations where the number of symbols used is significantly smaller than the number of possible symbols. It accepts symbol dictionaries of very large sizes (theoretically up to 2^256 although I have not tested this) and very small sizes. The header file allows for a wide range of flexibilty while keeping the size of the Huffman dictionary small. The tradeoff of the header is that very very small input data may be burdened by the size of the header (49 bits for an 8 bit symbol library). So if you are playing around with some foobar type variables, this would explain why the results may be a few bytes more than you expect.

It does not deal directly with files. This is because when I use the Huffman algorithm it is usually only one step in a multistep process. I have included some straightforward functions for reading and writing bytes to a file inside the demo code.

TO USE:
Start off with huffman_demo.py. I believe the implementation is fairly straightforward

TO DO:
I would like to implement more compression modes, such as a different format for the canonical code dictionary that works by recording just the bit size of each symbol in the alphabet or allowing for fixed Huffman dictionaries that are provided from external sources. 
