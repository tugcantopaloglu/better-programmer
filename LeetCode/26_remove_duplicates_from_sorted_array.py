class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        ln = len(nums)-1
        while ln > -1:
            if nums[ln] in seen:
                nums.remove(nums[ln])
            else:
                seen.append(nums[ln])
            ln -= 1
        return len(nums)

# SEEMS LIKE 3000MS BAD RUNTIME!
