import java.util.HashMap;
import java.util.Map;

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        
        // Count occurrences
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        int majority = 0;
        int maxCount = 0;
        
        // Find element with maximum count
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() > maxCount) {
                majority = entry.getKey();
                maxCount = entry.getValue();
            }
        }
        
        return majority;
    }
}
