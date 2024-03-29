# Canonical Huffman Compression

This implementation of the Huffman algorithm uses canonical code to save space. It is a full featured implementation that allows for the saving and loading of compressed files. It also allows for the use of a fixed dictionary, which can be useful in some situations.

Using canonical Huffamn codes allows us to save the Huffman code dictionary with a combination of sorted symbols and the number occurrences for each code length. This is ideal for situations where the number of symbols used is significantly smaller than the number of possible symbols.



# Example of how to use the HuffmanCoding class

This implementation expects inputs as a list of integers. In this example, we convert some text to integers using the python ord function.
```python
from canonical_huffman import HuffmanCoding
text = "Lorem ipsum dolor sit amet."
data = [ord(char) for char in text]
huff = HuffmanCoding()
huff.compress(data)
huff.save_compressed('example.bin')
# delete huff object and create a new one to show that there is no data leakage.
del huff
huff2 = HuffmanCoding()
huff2.open_compressed('example.bin')
decompressed = huff2.decompress_file()
if data == decompressed:
    print('huffman successful!')
else:
    print('huffman failed!')
```
# Example of how to use a fixed dictionary
A fixed dictionary is sometimes used when the data is fairly predictable across files e.g. the distribution of common letters in the English language. Fixed dictionaries can sometimes save space when the size of the dictionary is large compared to the size of the data. It is possible to implement a fixed dictionary with the current release, but it requires a little more work and management by the user.
```python
from canonical_huffman import HuffmanCoding
# First we need to create the fixed dictionary
huff_fixed = HuffmanCoding()
text = "Lorem ipsum dolor sit amet."
data = [ord(char) for char in text]
fixed_text = "the quick brown fox jumped over the lazy dogs, THE QUICK BROWN FOX JUMPED OVER THE LAZY DOGS."
fixed_data = [ord(char) for char in fixed_text]
huff_fixed.huff_dict.make_dictionary(fixed_data)
# Then we can compress the data with the fixed dictionary
huff_new = HuffmanCoding()
huff_new.huff_dict.canonical_codes = huff_fixed.huff_dict.canonical_codes
huff_new.compress(data, fixed_dict=True)
compressed_data = huff_new.encoded_text
# For now, it is up to the user to save the encoded binary text to a file as they see fit.
# The data should be much larger than the first example, since the fixed dictionary is not optimized for the data
print('Fixed dict compressed data size: ', len(compressed_data)//8)

```

