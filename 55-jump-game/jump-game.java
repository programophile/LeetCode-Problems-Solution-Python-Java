class Solution {
    public boolean canJump(int[] nums) {
        int max_index=0;
        for (int i=0;i<nums.length;i++){
            if (i>max_index){
                return false;
            }
            int index=0;
            index+=nums[i]+i;
            if (index>max_index){
                max_index=index;
            }
            
            
        }
        return true;
         

        
        
    }
}