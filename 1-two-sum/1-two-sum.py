class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i, n in enumerate(nums):
            if target - n in res:
                return i, res[target - n]
            res[n] = i