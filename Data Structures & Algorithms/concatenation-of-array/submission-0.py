class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        passes = 1

        while passes < 3:
            for i in range(len(nums)):
                ans.append(nums[i])
            passes += 1
        return ans