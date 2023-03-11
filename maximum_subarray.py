class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = int(-1*sys.maxsize)
        sumed = 0

        for num in nums:
            sumed += num
            max_sum = max(max_sum,sumed)

            if (sumed < 0):
                sumed = 0
        return max_sum
