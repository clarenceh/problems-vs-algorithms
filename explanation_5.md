# Problems vs Algorithms - Problem 5 - Autocomplete with Tries - Explanation

## Logic implemented
TrieNode and Trie classes were implemented.

Each TrieNode carries the following attributes:
1. A boolean attribute which indicates whether the chain of characters ended at this node indicates an end of word.
1. A dictionary with the character as the key and a pointer to the child TrieNode as the value. This indicates the possible characters for the suffix indicated by chaining the previous characters within it's parent TrieNode.

Each Trie carries the following attributes:
1. The root TrieNode which indicates the possible first characters of a word and pointer to their corresponding child TrieNode.

For the Trie class, the "insert" and "find" operations were implemented as follows:
1. For insert, we traverse the word for each character. We start at the root node. Then for each character, we check whether the character in the dictionary attribute of the TrieNode. If yes, we proceed to the corresponding child TrieNode and next character in the word. Otherwise, the character will be added to the dict attribute, and then a new TrieNode will be constructed as the child node of the character. At the end of word, we set the end_of_word boolean attribute to true.
1. For find, we traverse the Trie tree base on the character sequence in the prefix

For finding suffixes, the following logic was implemented:
1. Firstly, locate the TriNode base the character string that we want to search for suffixes.
1. Traverse the TrieNode tree under the TrieNode recursively and whenever we hit the end of word, we add the result suffix in the list of suffixes
1. Finally, we return the list of all possible suffixes.

## Run time complexity
For lookup, the worst case run time complexity is of O(n), where n is the no. of chars in the word.

## Space complexity
The memory requirements depends on the following factors:
1. The length of words (e.g. function, factory)
1. The unique no. of chars at the same level (e.g. fu, fa indicates different paths at the same level)
1. The no. of words (e.g. fun, functions, etc.)

As a result, the space complexity is of (O(word_length * unique_chars * no_of_words))
