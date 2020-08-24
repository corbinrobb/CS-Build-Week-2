class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create set to track integers that we find
        # (sets are implemented as hash tables in python)
        # as we iterate over the list check if int is in the set
        # if not then add it 
        # else is in then return True
        # if we make it through the whole list without finding dup
        # then return False
        
        found = set()
        
        for num in nums:
            if num not in found:
                found.add(num)
            else:
                return True
            
        return False