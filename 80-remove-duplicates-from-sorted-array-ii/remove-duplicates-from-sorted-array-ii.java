class Solution {
    public int removeDuplicates(int[] nums) {
        int index=2;
        for (int i=2;i<nums.length;i++){
            if (nums[index-2]!=nums[i]){
                // if (num)
                
                nums[index]=nums[i];
                index++;
                // if (nums[i]==nums[i+1]){
                //     index++;
                //     nums[index]=nums[i];
                // }
                // index=i-1;
            }

        }
        return index;
        
    }
}