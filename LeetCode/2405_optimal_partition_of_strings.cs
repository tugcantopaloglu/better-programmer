public class Solution {
    public int PartitionString(string s) {
        List < string > strArr = new List < string > ()
        string subStr = ""
        foreach(var i in s){
            if (subStr.Contains(i)){
                strArr.Add(subStr)
                subStr = ""
                subStr += i
            }
            else {
                subStr += i
            }
        }
        return strArr.Count+1
    }
}
