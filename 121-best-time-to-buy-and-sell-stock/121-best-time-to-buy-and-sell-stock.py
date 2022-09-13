class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                currentProfit = prices[r] - prices[l]
                res = max(res, currentProfit)
            else:
                l = r
            r += 1
        return res