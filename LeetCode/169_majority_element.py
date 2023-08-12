class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        for val in seen:
            if seen[val] > n:
                return int(val)
        return -1

# BAD MEMORY USAGE
