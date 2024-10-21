# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
from time import perf_counter

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(n+1):
            first = first.next
        while first:
            first = first.next
            second=second.next
        second.next = second.next.next
        return dummy.next

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
    # Example usage
    values = [1, 2, 3, 4, 5]
    n = 2
    
    head = create_linked_list(values)
    
    print("Original linked list:")
    print_linked_list(head)
    
    solution = Solution()
    
    start_time = perf_counter()
    result = solution.removeNthFromEnd(head, n)
    end_time = perf_counter()
    
    print(f"\nLinked list after removing {n}th node from the end:")
    print_linked_list(result)
    
    print(f"\nExecution time: {(end_time - start_time) * 1000:.6f} ms")
