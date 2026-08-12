# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        place = 1
        p1 = l1
        while p1:
            num1 += p1.val * place
            place*=10
            p1=p1.next
        
        num2 = 0
        place = 1
        p2 = l2
        while p2:
            num2 += p2.val * place
            place*=10
            p2=p2.next
        
        res = num1+num2
        # print(res,num1,num2)
        if res == 0: #if res zero, return single listNode
            return ListNode(val=0)
        
        dummyHead = ListNode()
        curr = dummyHead

        while res > 0:
            nextNode = ListNode(val=res%10)
            curr.next = nextNode
            curr = curr.next
            res//=10
        return dummyHead.next
        
        # #cast to str and reverse
        # ans = str(ans)[::-1]
        # # print(ans)
        # #now make linked list
        # head = ListNode(int(ans[0]))
        # curr = head
        # for i in range(1,len(ans)):
        #     temp = ListNode(int(ans[i]))
        #     curr.next = temp
        #     curr = temp
        # return head


        
        