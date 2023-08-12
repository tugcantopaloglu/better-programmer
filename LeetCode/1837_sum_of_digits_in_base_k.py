class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sub = 0
        quo = n
        newNumber = ""
           if k != n:
                while quo > 0:
                    modulus = quo % k
                    quo = quo // k
                    newNumber += str(modulus)
                str_array = [*newNumber]
                for i in str_array:
                    sub += int(i)
                return sub+quo
            elif k == 10:
                str_version = str(n)
                sub = 0
                str_array = [*str_version]
                for i in str_array:
                    sub += int(i)
                return sub
            else:
                return 1
