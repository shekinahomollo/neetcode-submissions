class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n) #map the numbers to their frequency

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: #for every value that is present in the frequency map
                res.append(n)
                if len(res) == k:
                    return res