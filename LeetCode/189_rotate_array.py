class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > 0:
            nums.insert(0, nums.pop())
            k -= 1
            Solution.rotate(self, nums, k)
