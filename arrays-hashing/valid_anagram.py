# Time: O(n + m), where n is s string length while m is t string length
# Space: O(n + m), since extra space is required to store n chars and m chars

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        chars = {}
        charsAux = {}


        for c in s:
            if c not in chars: 
                chars[c] = 1
            else:
                chars[c] += 1

        
        for c in t:
            if c not in charsAux: 
                charsAux[c] = 1
            else:
                charsAux[c] += 1

    
        for c in chars:
            if c not in charsAux: return False
            if chars[c] != charsAux[c]: return False

        return True 
