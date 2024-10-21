# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        ol=[]
        while curr!=None:
            ol.append(curr)
            curr=curr.next
        if len(ol)<3:
            return head
        left=len(ol)-2
        right =1
        gate=True
        curr = head
        curr.next=ol[-1]
        curr=curr.next
        # print(0,end=" ")
        while right<=left:
            # print(f"right:{right},left:{left}")
            if gate:
                # print(right,end=" ")
                curr.next=ol[right]
                right+=1
                gate = False
                
            else:
                # print(left,end=" ")
                curr.next=ol[left]
                left-=1
                gate = True
                
            # print(curr.val)
            curr=curr.next
        curr.next=None
        # curr = head
        # while curr!=None:
        #     print(curr.val,"->",end="")
        #     curr=curr.next
    def slow_fast_pointer(self,head:Optional[ListNode])->Optional[ListNode]:
        if not head or not head.next:
            return head
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        second  =  slow.next
        slow.next=None
        prev=None
        while second:
            temp = second.next
            second.next=prev
            prev=second
            second = temp
        first,second = head,prev
        while second:
            temp1,temp2 = first.next,second.next
            first.next=second
            second.next = temp1
            second,first = temp2,temp1
        return head
        
            
        

# Driver code
if __name__ == "__main__":
    import time

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

    # Example
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)

    print("Original list:")
    print_linked_list(head)

    solution = Solution()

    start_time = time.perf_counter()
    solution.reorderList(head)
    end_time = time.perf_counter()

    print("Reordered list:")
    print_linked_list(head)

    print(f"Execution time: {(end_time - start_time) * 1000:.2f} ms")
    print(f"Second solution")
    start_time = time.perf_counter()
    solution.slow_fast_pointer(head)
    end_time = time.perf_counter()
    print_linked_list(head)
    print(f"Execution time: {(end_time - start_time) * 1000:.2f} ms")
