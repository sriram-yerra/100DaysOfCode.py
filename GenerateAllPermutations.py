def permute(nums):
    if len(nums) == 1:     # Base case
        return [nums[:]]
    result = []
    for i in range(len(nums)):
        current = nums[i]  # Choose the current element as the first element
        remaining = nums[:i] + nums[i+1:]  # Generate permutations for the rest of the elements
        permutations_of_remaining = permute(remaining)
        for perm in permutations_of_remaining:  # Combine the current element with each permutation of the remaining elements
            result.append([current] + perm)
    return result
# Example usage:
nums = [1, 2, 3]
result = permute(nums)
print(result)
