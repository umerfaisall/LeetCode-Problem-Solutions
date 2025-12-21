# my approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        res = []
        while prev is not None:
            res.append(prev.val)
            prev= prev.next
        index_number_to_remove = len(res) - n
        remove = res[index_number_to_remove]
        print(remove)
        if head.val == remove:
              return head.next
        previous = head
        current = previous.next
        while current is not None and current.val != remove:
            previous = previous.next
            current = previous.next
        if current is not None and current.val == remove:
            previous.next =current.next
        return head
# fails at test case where there are multiple "remove" values in the list

fast = head
slow = head
for _ in range(n):
    fast = fast.next
if fast == None:
    return head.next
while fast.next is not None:
    fast = fast.next
    slow = slow.next
slow.next = slow.next.next
return head

# actual solution