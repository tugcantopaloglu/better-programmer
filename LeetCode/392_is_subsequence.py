class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        clear_t = ""
        for i in t:
            if i in [*s]:
                clear_t += i
        if s in clear_t: 
            return True
        else: 
            return False
        #Case 16 in leetcode has an error which gives wrong answer
