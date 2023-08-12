class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ln = len(nums)-1
        dic = {}
        while ln > -1:
            if nums[ln] in dic:
                dic[nums[ln]] += 1
                if dic[nums[ln]] > 2:
                    del nums[ln]
            else:
                dic[nums[ln]] = 1
            ln -= 1
