class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxCount, res = 0, 0
        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if count[num] > maxCount:
                res = num
            else:
                res

            maxCount = max(maxCount, count[num])
        
        return res