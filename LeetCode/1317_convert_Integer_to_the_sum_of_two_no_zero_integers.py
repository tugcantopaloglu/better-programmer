class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        list = [0, 0]
        list[0] = 1
        list[1] = n-1
        while ("0" in str(list[1])) or ("0" in str(list[0])):
            list[0] += 1
            list[1] -= 1
        return list
