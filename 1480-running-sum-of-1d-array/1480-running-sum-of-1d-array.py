class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        s = 0
        for i in nums:
            s += i
            res.append(s)
        return res