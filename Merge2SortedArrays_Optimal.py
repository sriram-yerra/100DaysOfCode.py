class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # Pointer for nums1
        j = n - 1  # Pointer for nums2
        k = m + n - 1  # Pointer for the result, starting from the end of nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2
        for p in range(j, -1, -1):
            nums1[k] = nums2[p]
            k -= 1

        return nums1
sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
result = sol.merge(nums1, m, nums2, n)
print(result)
