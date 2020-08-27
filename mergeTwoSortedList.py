class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = []
        
        current_a = l1
        current_b = l2
        
        while current_a and current_b:
            if current_a.val <= current_b.val:
                merged.append(current_a)
                current_a = current_a.next
            else:
                merged.append(current_b)
                current_b = current_b.next
        
        if current_a and not current_b:
            while current_a:
                merged.append(current_a)
                current_a = current_a.next
                
        if current_b and not current_a:
            while current_b:
                merged.append(current_b)
                current_b = current_b.next
        
        
        for i in range(len(merged)):
            if i == len(merged) - 1:
                merged[i].next = None
            else:
                merged[i].next = merged[i + 1]
        
        if len(merged) == 0:
            if current_a:
                return current_a
            else:
                return current_b
        else:
            return merged[0]
            