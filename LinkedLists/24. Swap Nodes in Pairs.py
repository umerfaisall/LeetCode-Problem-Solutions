# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        current = head
        while current and current.next:
            #next pair
            nextPair = current.next.next
            second = current.next 

            #swapping 
            current.next = nextPair
            second.next = current 
            prev.next = second

            #updating pointers
            prev = current
            current = nextPair 
        return dummy.next 