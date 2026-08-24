class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        write_pos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[write_pos - 2]:
                nums[write_pos] = nums[i]
                write_pos += 1
        return write_pos