# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # walk through both linked lists at same time
        # create new list using sum of values
        # iterate over list and carry over values when greater than 10
        # iterate over list again and create Linked List with values
        # return new Linked List
        
        current1 = l1
        current2 = l2
        l = []

        while current1 and current2:
            l.append(current1.val + current2.val)
            
            current1 = current1.next
            current2 = current2.next
            if not current1 and current2:
                while current2:
                    l.append(current2.val)
                    current2 = current2.next
                break
                    
            if not current2 and current1:
                while current1:
                    l.append(current1.val)
                    current1 = current1.next
                break
                
        start = None
        cur = None
        
        for i, n in enumerate(l):
            if n >= 10:
                if i + 1 < len(l):
                    l[i + 1] += n // 10
                else:
                    l.append(n // 10)
                l[i] = n % 10
            if not start:
                start = ListNode(l[i])
                cur = start
            else:
                cur.next = ListNode(l[i])
                cur = cur.next
        

            
        
        return start