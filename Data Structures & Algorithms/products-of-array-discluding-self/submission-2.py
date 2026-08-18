class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        # First pass: store prefix products in result
        result[0] = 1
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Second pass: multiply suffix products in-place
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result