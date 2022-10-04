# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        temp=self
        arr=[]
        while(temp!=None):
            arr.append(temp.val)
            temp=temp.next
        arr=[str(i) for i in arr]
        return ''.join(arr)
class Solution:
    def addTwoNumbers(self, l1, l2):
        c=0
        r=0
        ans=start=ListNode(0)
        while(l1 and l2):
            ans.next=ListNode((l1.val+l2.val+c)%10)
            c=(l1.val+l2.val+c)//10
            # r=(l1.val+l2.val+c)%10
            ans=ans.next
            l1=l1.next
            l2=l2.next
        if l1:
            if c:
                while(l1):
                    ans.next=ListNode((l1.val+c)%10)
                    c=(l1.val+c)//10
                    # r=(l2.val+c)%10
                    ans=ans.next
                    l1=l1.next

            if c:
                ans.next=ListNode(c)
        elif l2:
            if c:
                while(l2):
                    ans.next=ListNode((l2.val+c)%10)
                    c=(l2.val+c)//10
                    # r=(l2.val+c)%10
                    ans=ans.next
                    l2=l2.next
                    print('hrer')
            if c:
                ans.next=ListNode(c)
        else:
            pass
        return start.next

x1=ListNode(2)
x1.next=ListNode(4)
x1.next.next=ListNode(9)
x2=ListNode(5)
x2.next=ListNode(6)
x2.next.next=ListNode(4)
x2.next.next.next=ListNode(9)

a=Solution()
print(a.addTwoNumbers(x1,x2))