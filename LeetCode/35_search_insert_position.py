class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            sol = nums.index(target)
            return int(sol)
        except Exception as e:
            for i in nums[::-1]:
                if i < target:
                    return int(nums.index(i))+1
                elif i == nums[0]:
                    return 0
