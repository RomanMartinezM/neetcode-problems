# 1. Brute Force

# Time & Space Complexity
# Time complexity: O(n2)
# Space complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []


# 2. Binary Search

# Time & Space Complexity
# Time complexity: O(nlog⁡n)
# Space complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []


# 3. Hash Map

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []

# 4. Two Pointers

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []