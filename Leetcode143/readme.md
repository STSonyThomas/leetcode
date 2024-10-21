# Reorder List Solution

## Approaches
1. Array Manipulation
2. Slow-Fast Pointer

### 1. Array Manipulation Approach
* Uses a combination of array manipulation and linked list traversal
* Time Complexity: O(n), where n is the length of the linked list
* Space Complexity: O(n) for the array storage
* Concepts: Linked Lists, Two Pointer Technique

### 2. Slow-Fast Pointer Approach
* Uses in-place manipulation of the linked list
* Time Complexity: O(n), where n is the length of the linked list
* Space Complexity: O(1), as it only uses a constant amount of extra space
* Concepts: Linked Lists, Two Pointer Technique, Reversing Linked List

[Link to problem](https://leetcode.com/problems/reorder-list/)
<u>Leetcode Problem Number #143</u>
**STATUS**: _Accepted_

## Algorithm Explanations

### 1. Array Manipulation Algorithm
1. Traverse the linked list and store all nodes in an array.
2. If the list has less than 3 nodes, return the original list.
3. Initialize two pointers: 'left' at the second-to-last element and 'right' at the second element.
4. Reorder the list by alternating between:
   - Connecting the current node to the last unconnected node from the end.
   - Connecting the current node to the next unconnected node from the beginning.
5. Continue until all nodes are connected in the new order.
6. Set the last node's next pointer to None to terminate the list.

This algorithm efficiently reorders the list in a single pass through the array, utilizing the benefits of random access in the array.

### 2. Slow-Fast Pointer Algorithm
1. Use slow and fast pointers to find the middle of the list.
2. Split the list into two halves at the middle.
3. Reverse the second half of the list.
4. Merge the two halves by alternating nodes.

This algorithm reorders the list in-place without using extra space, making it more memory-efficient.

## Implementation Details
The solution is implemented in Python. It uses the `typing` module for type hinting and the `Optional` type for the linked list nodes.

The `Solution` class contains two methods:
1. `reorderList`: Implements the array manipulation approach.
2. `slow_fast_pointer`: Implements the slow-fast pointer approach.

The driver code demonstrates how to use both solutions, creates a sample linked list, reorders it using both methods, and provides execution time measurements using the `time` module.

## Performance Comparison
The driver code includes timing for both approaches, allowing for a direct comparison of their performance. While both have O(n) time complexity, the slow-fast pointer method may be faster in practice due to better cache utilization and no array allocation overhead.
