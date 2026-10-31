# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            a = curr.val
            b = curr.next.val
            temp = curr.next

            gcd = math.gcd(a,b)
            insertNode = ListNode(gcd)

            curr.next = insertNode
            insertNode.next = temp
            curr = temp
        
        return head