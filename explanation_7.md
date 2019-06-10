# Problems vs Algorithms - Problem 7 - Request Routing in a Web Server with a Trie - Explanation

## Logic implemented
RouteTrieNode, RouteTrie and Router classes were implemented.

Each RouteTrieNode carries the following attributes:
1. A handler attribute (of type string) which indicates whether there exist a handler at this node (for the path which is compose of the sub-paths of parent nodes).
1. A dictionary with the possible sub-paths as the key and a pointer to the child RouteTrieNode as the value. This indicates the possible child paths of the current node.

Each RouteTrie carries the following attributes:
1. The root RouteTrieNode which indicates the possible first sub-paths and a pointer to their corresponding child TrieNode.

For the RouteTrie class, the "insert" and "find" operations were implemented as follows:
1. For insert, we traverse the path for each sub-path (split with the "/" character). We start at the root node. Then for each sub-path, we check whether the sub-path is in the dictionary attribute of the RouteTrieNode. If yes, we proceed to the corresponding child RouteTrieNode and next sub-path. Otherwise, the sub-path will be added to the dict attribute, and then a new RouteTrieNode will be constructed as the child node of the sub-path. At the end of path, we set the handler attribute accordingly.
1. For find, we traverse the RouteTrie tree base on the sub-path sequence

For finding handler with the Router class, the following logic was implemented:
1. Firstly, locate the RouteTriNode base the path string (split using the "/" character) that we want to search.
1. If RouteTriNode for the path was not found in the RouteTrie, return "not found handler"
1. If RouteTriNode for the path was found and the handler attribute is not None, then return the attribute as the handler.

## Run time complexity
For Trie approach, the run time complexity of insert and search is of O(n), where n is the number of tokens upon splitting the path with "/" character.

## Space complexity
The memory requirements depends on the following factors:
1. The no. of tokens in the path (e.g. /home/about contains 2 tokens)
1. The unique no. of tokens (e.g. /home, /me, /you indicates different paths at the same level)
1. The length of the token (e.g. home, about, etc.)

As a result, the space complexity is of (O(token_length * unique_tokens * no_of_tokens))
