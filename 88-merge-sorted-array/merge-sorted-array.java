class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // int[] new_arr = new int[m+n];
        int m_index=m-1;
        int n_index=n-1;
        int right_index=m+n-1;
        while (n_index>=0){
            if (m_index>=0 && nums1[m_index]>nums2[n_index]){
                nums1[right_index]=nums1[m_index];
                m_index-- ;
            }else{
                nums1[right_index]= nums2[n_index] ;
                n_index-- ;
            }
            right_index-- ;
        }



        
    }
}