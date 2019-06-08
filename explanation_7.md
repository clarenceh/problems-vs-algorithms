# Problems vs Algorithms - Problem 7 - Request Routing in a Web Server with a Trie - Explanation

## Logic implemented
RouteTrieNode, RouteTrie and Router classes were implemented.

## Run time complexity
For Trie approach, the run time complexity of insert and search is of O(n), where n is the number of tokens upon splitting the path with "/" character.

## Space complexity
The memory requirements depends on the following factors:
1. The no. of tokens in the path (e.g. /home/about contains 2 tokens)
1. The unique no. of tokens (e.g. /home, /me, /you indicates different paths at the same level)
1. The length of the token (e.g. home, about, etc.)

As a result, the space complexity is of (O(token_length * unique_tokens * no_of_tokens))
