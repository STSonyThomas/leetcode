# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        steps = 0  # Performance counter
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            steps += 1
            if slow == fast:
                print(f"Cycle detected after {steps} steps")
                return True
        
        print(f"No cycle found after {steps} steps")
        return False
        
# Example usage
def create_test_case(values, pos):
    if not values:
        return None
    
    # Create nodes
    nodes = [ListNode(val) for val in values]
    
    # Link nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if pos is valid
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

# Test cases
head1 = create_test_case([3,2,0,-4], 1)  # Has cycle
head2 = create_test_case([1,2], 0)       # Has cycle
head3 = create_test_case([1], -1)        # No cycle

solution = Solution()
print("Test case 1:", solution.hasCycle(head1))  # True
print("Test case 2:", solution.hasCycle(head2))  # True
print("Test case 3:", solution.hasCycle(head3))  # False
