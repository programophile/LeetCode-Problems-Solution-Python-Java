class Solution {
    public int countValidSelections(int[] nums) {
        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                int leftSum = 0;
                for (int j = 0; j < i; j++) {
                    leftSum += nums[j];
                }

                int rightSum = 0;
                for (int j = i; j < nums.length; j++) {
                    rightSum += nums[j];
                }

                if (leftSum == rightSum) {
                    count += 2;
                } else if (Math.abs(leftSum - rightSum) == 1) {
                    count += 1;
                }
            }
        }

        return count;
    }
}
