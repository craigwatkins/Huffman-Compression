"""
Dictionary class
properties: huffman_tree, huffman_dictionary, canonical huffman dictionary
methods: build_huffman_tree, build_huffman_dictionary, build_canonical_huffman_dictionary, get_canonical_huffman_dictionary
"""


class Dictionary:
    def __init__(self):
        self.huffman_tree = None
        self.huffman_dictionary = None
        self.canonical_huffman_dictionary = None

    def build_huffman_tree(self, node_heap):
        """
        Parameters
        ----------
        occurrences : Dictionary
            Key - Symbols represented by integer values
            Value - number of times that the symbol occurs in the data

        Returns
        -------
        None.

        """
        node_heap = []
        for key in occurrences:
            node = Node(key, occurrences[key])
            heapq.heappush(node_heap, node)
        return node_heap


