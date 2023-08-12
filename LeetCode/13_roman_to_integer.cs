public class Solution {
    private readonly Dictionary<char, int> dict = new Dictionary<char, int>{{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
    
    public int RomanToInt(string s) {
   
        char[] ch = s.ToCharArray();
    
        int result = 0;
        int intVal,nextIntVal;
            
        for(int i = 0; i <ch.Length ; i++){
            intVal = dict[ch[i]];
            
            if(i != ch.Length-1)
            {
                nextIntVal = dict[ch[i+1]];
                
                if(nextIntVal>intVal){
                    intVal = nextIntVal-intVal;
                    i = i+1;
                }
            }
             result = result + intVal;
        }
        return result;
    }
}