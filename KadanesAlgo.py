class MaxSubArrSum():
    def maxsub(self,arr):
        max = 0
        sum = 0
        for i in range(len(arr)):
            sum = sum + arr[i]
            if sum < 0:
                sum = 0
            if sum > max:
                max = sum

        # Check if all elements in the array are negative
        if max == 0:
            if all(num < 0 for num in arr):
                return max(arr)
        else:
            return max

        #return max

arr = [-1,-2,3]
msa = MaxSubArrSum()
res = msa.maxsub(arr)
print(res)