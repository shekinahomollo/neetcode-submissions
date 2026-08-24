class Solution(object):
    def majorityElement(self, nums):
        res = []
        count = Counter(nums)

        for key in count:
            if count[key] > len(nums)//3:
                res.append(key)

        return res