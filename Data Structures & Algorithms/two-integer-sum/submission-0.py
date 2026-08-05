class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in numMap and numMap[diff] != i:
                return [i, numMap[diff]]

        return []