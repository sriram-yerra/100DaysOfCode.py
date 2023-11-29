class Solution():
    def maxProfit(self, prices):
        c = 0
        a = 0
        b = len(prices) - 1
        while b > a:
            if prices[a] > prices[b]:
                a+=1
            if prices[a] < prices[b]:
                r = prices[b] - prices[a]
                c = max(c,r)
                b-=1
        return c

arr = [7,1,5,3,6,4]
sol = Solution()
res = sol.maxProfit(arr)
print(res)