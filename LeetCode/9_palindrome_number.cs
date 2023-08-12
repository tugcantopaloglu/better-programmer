public class Solution {
    public bool IsPalindrome(int x) {
        int reversed = 0;
        int remainder = 0;
        int copy = x;
        if(x < 0){
            return false;
        }
        else{
            while (copy != 0){
                remainder = copy % 10;
                reversed = reversed * 10 + remainder;
                copy /= 10;
            }
            if(reversed == x){
                return true;
            }
        }
        return false;
    }
}