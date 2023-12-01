class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return nums[i]


nums = [1,3,4,2,2]
sol = Solution()
res = sol.findDuplicate(nums)
print(res)