# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (head==None):
            return head
        temp =head
        ptemp = head
        count=0
        while(temp!=None):
            count+=1
            temp=temp.next
        k = count-n+1
        if (k==1):
            head = head.next
            return head
        for i in range(1,k-1):
            ptemp=ptemp.next
        if (ptemp.next!=None):
            ptemp.next=ptemp.next.next;
        return head
        
