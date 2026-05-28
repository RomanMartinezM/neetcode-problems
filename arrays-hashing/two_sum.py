
# Time complexity: O(n), where n is the number of elements in the array
# Space complexity: O(n), since we need to create a hash map to store the value and index of each element in the array.

#Constraints: i != j and nums[i] + nums[j] == target
#Approach: difference = target - nums[i]

# Solution 1 (Two Pass)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []

            

# solution 2 (One Pass)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return [i, indices[diff]]
            indices[n] = i
