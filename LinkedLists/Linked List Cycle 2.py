# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_map = {}
        temp = head
        while temp is not None:
            if temp in hash_map:
                return temp
            hash_map[temp] =1
            temp = temp.next
        return None