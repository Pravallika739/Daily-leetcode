class Solution {
    public int maxProfit(int[] a) {
        int profit=0,buy=a[0],cnt=0;
        for(int i=0;i<a.length;i++){
            if(buy>a[i]){
                buy=a[i];
            }
            else{
                profit=Math.max(profit,a[i]-buy);
            }
        }
        return profit;
    }
}