# hashmap stretegy

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_map = {}
        temp = head
        while temp is not None:
            if temp in hash_map:
                return True
            hash_map[temp] =1
            temp = temp.next
        return False
# Time Complexity = O(nlogn)
# Space Complexity = O(n)