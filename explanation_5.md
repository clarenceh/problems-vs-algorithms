# Problems vs Algorithms - Problem 5 - Autocomplete with Tries - Explanation

## Logic implemented
TrieNode and Trie classes were implemented.

## Run time complexity
For lookup, the worst case run time complexity is of O(n), where n is the no. of chars in the word.

## Space complexity
The memory requirements depends on the following factors:
1. The length of words (e.g. function, factory)
1. The unique no. of chars at the same level (e.g. fu, fa indicates different paths at the same level)
1. The no. of words (e.g. fun, functions, etc.)

As a result, the space complexity is of (O(word_length * unique_chars * no_of_words))
