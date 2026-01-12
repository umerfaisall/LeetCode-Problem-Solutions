class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=set(nums)
        m = 1
        while m in x:
            m+=1
        return m
