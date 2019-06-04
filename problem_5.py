## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie

        # A dictionary to store the possible characters in this node
        # Dictionary key: character (e.g. a)
        # Dictionary value: a tuple (end_of_word: boolean, child_node)
        self.char_dict = dict()

    def insert(self, char):
        ## Add a child node in this Trie
        pass


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = None

    def insert(self, word):
        ## Add a word to the Trie
        pass

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        pass


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
