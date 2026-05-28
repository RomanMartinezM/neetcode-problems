# Time: O(n), where n is the length of nums
# Space: O(n), since require to store each different num in a dictionary


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = {}

        for n in nums:
            if n in exist: return True
            exist[n] = 1
        
        return False



