public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices.Length <= 1) {
            return 0; 
        }
        int minPrice = prices[0]; 
        int maxProfit = 0; 

        for (int i = 1; i < prices.Length; i++) {
            int currentPrice = prices[i];
            if (currentPrice < minPrice) {
                minPrice = currentPrice; 
            } else {
                int profit = currentPrice - minPrice;
                if (profit > maxProfit) {
                    maxProfit = profit; 
                }
            }
        }

        return maxProfit;
    }
}


/*
SLOW SOLUTION
    public int MaxProfit(int[] prices) {
        int result = 0;
        for (int i = 0; i< prices.Length; i++){
            for (int j = i; j< prices.Length; j++){
                if (prices[j] - prices[i] > result && i < j){
                    result = prices[j] - prices[i];
                }
            }
        }
        if (result <= 0){ return 0;}
        else {return result;}
        
    }
*/
