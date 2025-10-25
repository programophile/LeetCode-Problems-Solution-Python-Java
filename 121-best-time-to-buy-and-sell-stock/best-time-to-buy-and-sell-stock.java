class Solution {
    public int maxProfit(int[] prices) {
        int buy_index=0; //will try to keep it lowest
        int sell_index=0; //keep it highest 
        int final_profit=0;
        while(sell_index<prices.length){
            int profit=prices[sell_index]-prices[buy_index];
            if (prices[buy_index]>prices[sell_index]){
                buy_index=sell_index;
            }
            if (profit>final_profit){
                final_profit=profit;
            }
            sell_index++;
        }
        return final_profit;
    }
}