
# Solution 1: 1. Sorting
# Time complexity: O(m * n), where m is the number of strings while n is the lenght of each string
# Space complexity: O(m), where m is the number of strings
# Where m is the number of strings and n is the length of the longest string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            groups[sortedS].append(s)

        return list(groups.values())



# Solution 2: 2. Hash Table
# Time complexity: O(m * n), where m is the number of strings while n is the lenght of each string
# Space complexity: 
#   - O(m), auxiliary space, excluding the returned output.
#   - O(m * n),  total space if the output groups are counted.
# Where m is the number of strings and n is the length of the longest string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            letters = [0]*26 #lowercase letters
            for c in s:   
                letters[ord(c) - ord('a')] += 1
            groups[tuple(letters)].append(s)
        
        return list(groups.values())



