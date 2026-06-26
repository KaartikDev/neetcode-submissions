# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        p1 = l1
        i = 0
        while p1:
            i+=1
            num1+=str(p1.val)
            p1 = p1.next
        
        p2 = l2
        while p2:
            i+=1
            num2+=str(p2.val)
            p2 = p2.next
        
        #Cast the REVERSED string (via -1 stride val)
        # print(num1,num2)
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        # print(num1,num2)
        ans = num1 + num2
        # print(num1,num2,ans)

        #cast to str and reverse
        ans = str(ans)[::-1]
        # print(ans)
        #now make linked list
        head = ListNode(int(ans[0]))
        curr = head
        for i in range(1,len(ans)):
            temp = ListNode(int(ans[i]))
            curr.next = temp
            curr = temp
        return head


        
        