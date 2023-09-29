class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (s == ""): return True
        pol_string = ""
        normal_string = ""
        s = s.lower()
        alp_tuple = {'a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','r','s','t','u','v','y','z','w','q','i','x','1','2','3','4','5','6','7','8','9','0'}
        for i in range(len(s)-1,-1,-1):
            if s[i] in alp_tuple:
                pol_string += s[i]
        for i in range(len(s)):
            if s[i] in alp_tuple:
                normal_string += s[i]
        print(normal_string)
        print(pol_string)
        if (pol_string == normal_string):
            return True
        else:
            return False
        
