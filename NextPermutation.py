class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3 and Step 4
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums

# Example usage:
# solution = Solution()
# nums = [1, 2, 3]
# result = solution.nextPermutation(nums)
# print(result)


