# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
import time

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

# Driver code
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Example input
    values = [1, 2, 3, 4, 5]
    
    # Create the linked list
    head = create_linked_list(values)
    
    print("Original linked list:")
    print_linked_list(head)
    
    # Create a Solution instance
    solution = Solution()
    
    # Measure execution time
    start_time = time.perf_counter()
    
    # Reverse the linked list
    reversed_head = solution.reverseList(head)
    
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    print("\nReversed linked list:")
    print_linked_list(reversed_head)
    
    print(f"\nExecution time: {execution_time:.6f} ms")