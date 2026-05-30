
# Time complexity: O(nlogn)
# Space complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        return list(sorted(freq, key=freq.get, reverse=True)[:k])
        
       