from typing import Optional
from time import perf_counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        current =  ans
        while list1 and list2:
            if list1.val<=list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next =list2
                list2=list2.next
            current = current.next
        if list1:
            current.next=list1
        elif list2:
            current.next=list2
        return ans.next

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
    list1_values = [1, 2, 4]
    list2_values = [1, 3, 4]
    
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    
    solution = Solution()
    
    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)
    
    start_time = perf_counter()
    merged_list = solution.mergeTwoLists(list1, list2)
    end_time = perf_counter()
    
    print("Merged List:")
    print_linked_list(merged_list)
    
    print(f"Time taken: {(end_time - start_time) * 1000:.6f} ms")

