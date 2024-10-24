# Linked List Cycle

## Approach
This solution uses the Floyd's Cycle-Finding Algorithm, also known as the "tortoise and hare" algorithm.

1. We use two pointers: `slow` and `fast`.
2. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps.
3. If there's a cycle, the `fast` pointer will eventually meet the `slow` pointer.
4. If there's no cycle, the `fast` pointer will reach the end of the list.

## Time Complexity
- O(n), where n is the number of nodes in the linked list.
- In the worst case, when there is no cycle, we traverse each node once.
- If there is a cycle, we may traverse most nodes twice before detecting the cycle.

## Space Complexity
- O(1), as we only use two pointers regardless of the input size.

## Performance Optimization
- A step counter is included to measure the number of iterations before detecting a cycle or reaching the end of the list.
- This can be useful for performance analysis but doesn't affect the core algorithm.

## Test Cases
The solution includes a `create_test_case` function to easily create linked lists with or without cycles for testing purposes.

[Link to problem](https://leetcode.com/problems/linked-list-cycle/)

<u>Leetcode Problem Number #141</u>

**STATUS**: _Accepted_
