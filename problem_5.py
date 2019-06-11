# Represents a single node in the Trie
class TrieNode:
    def __init__(self, end_of_word=False):
        # Initialize this node in the Trie

        # Indicates whether the string ends here is a valid word
        self.end_of_word = end_of_word

        # A dictionary to store the possible characters in this node
        # Dictionary key: character (e.g. a)
        # Dictionary value: pointer to child node
        self.char_dict = dict()

    def insert(self, char):
        # Add a child node in this Trie
        sub_char_node = TrieNode()
        self.char_dict[char] = sub_char_node

        return sub_char_node

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        output_str_list = list()

        def find_suffix(node, output_str):

            # If end_of_word at this node is true, then add the suffix to result list
            if node.end_of_word:
                output_str_list.append(output_str)

            for char in node.char_dict:
                temp_output_str = output_str + char
                find_suffix(node.char_dict[char], temp_output_str)

        find_suffix(self, "")

        return output_str_list


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        root_node = TrieNode()
        self.root = root_node

    def insert(self, word):
        # Add a word to the Trie

        # Split the word into a seq of chars and build the corresponding TrieNodes
        cur_node = self.root

        for char in word:
            if char in cur_node.char_dict:
                cur_node = cur_node.char_dict[char]
            else:
                new_child_node = cur_node.insert(char)
                cur_node = new_child_node

        # End of word, set end_of_word property to True
        cur_node.end_of_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix

        cur_node = self.root
        # Traverse the Trie tree base on the character sequence in the prefix
        for char in prefix:
            if char in cur_node.char_dict:
                cur_node = cur_node.char_dict[char]
            else:
                return None

        return cur_node

    def __str__(self):
        output_str = [""]

        def print_node(node, output_str):
            output_str[0] += f"\nEnd of word: {node.end_of_word}\n"
            for char in node.char_dict:
                output_str[0] += f"char: {char}"
                print_node(node.char_dict[char], output_str)

        print_node(self.root, output_str)

        return output_str[0]


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

node = MyTrie.find('f')
print(node.suffixes())
