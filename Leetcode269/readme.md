# Alien Dictionary Solution

1. **Approach**
   * Build a graph of character relationships from the given words
   * Perform topological sort using DFS
   * Detect cycles to handle invalid orders
   * Time complexity: O(C), where C is the total length of all words combined
   * Concepts: Graph, DFS, Topological Sort, Hashmap

[Link to problem](https://leetcode.com/problems/alien-dictionary/)
<u>Leetcode Problem Number #269</u>
**STATUS**: _Accepted_

## Key Points:
* Uses a defaultdict to create a graph of character relationships
* Implements cycle detection to handle invalid dictionary orders
* Utilizes depth-first search (DFS) for topological sorting
* Handles edge cases like prefix words

## Performance:
* Time: [Insert actual runtime here] ms
* Memory: [Insert actual memory usage here] MB

## Notes:
* The solution assumes that the input is valid and follows the problem constraints
* An empty string is returned for invalid orders (e.g., cycles or prefix word issues)
