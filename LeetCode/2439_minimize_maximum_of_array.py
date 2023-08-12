class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        answer = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            answer = max(answer, math.ceil(prefix_sum / (i + 1)))

        return answer
