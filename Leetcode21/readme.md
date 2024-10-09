# Merge Two Sorted Lists Solution

## Approach
* Uses iterative comparison and merging of two sorted linked lists
* Time Complexity: O(n + m), where n and m are the lengths of the input lists
* Space Complexity: O(1)
* Concepts: Linked Lists, Two Pointer Technique

[Link to problem](https://leetcode.com/problems/merge-two-sorted-lists/)
<u>Leetcode Problem Number #21</u>
**STATUS**: _Accepted_

## Algorithm Explanation
The algorithm for merging two sorted linked lists works as follows:
1. Create a dummy node as the head of the result list.
2. Initialize a current pointer to the dummy node.
3. While both input lists have nodes:
   - Compare the values of the current nodes in both lists.
   - Append the node with the smaller value to the result list.
   - Move to the next node in the list that provided the smaller value.
4. If any list still has remaining nodes, append them to the result list.
5. Return the next node of the dummy node (which is the actual head of the merged list).

This algorithm is efficient as it merges the lists in a single pass and uses constant extra space.

## Implementation Details
The solution is implemented in Python. It uses the `typing` module for type hinting and the `perf_counter` function from the `time` module to measure execution time.

The `mergeTwoLists` function in the `Solution` class implements the merging algorithm. The driver code demonstrates how to use the solution, creates sample linked lists, merges them, and provides execution time measurement.

