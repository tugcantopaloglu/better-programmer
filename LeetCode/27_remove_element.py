class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        metric = len(nums)-1
        while metric > -1:
            if nums[metric] == val:
                del nums[metric]
            metric -= 1
        return len(nums)
