class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            s = 0
            for j in range(i+1):
                s += nums[j]
            res.append(s)
        return res