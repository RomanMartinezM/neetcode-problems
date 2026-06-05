from typing import List

# Solution 1: 1. Encoding & Decoding

# Time complexity: O( m + n) for each encode() and decode() function calls
# Space complexity: O( m + n) for each encode() and decode() function calls
# Where m is the sum of lengths of all the strings and n is the number of strings.

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res

    

# Solutio 2: 2. Encoding & Decoding (Optimal)

# Time complexity: O( m + n) for each encode() and decode() function calls
# Space complexity: O( m + n) for each encode() and decode() function calls
# Where m is the sum of lengths of all the strings and n is the number of strings.

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res