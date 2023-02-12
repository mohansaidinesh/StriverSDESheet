import java.util.Arrays;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int i=0;i<n;i++){
            nums1[m++]=nums2[i];
        }
        Arrays.sort(nums1);
    }
}





class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k=0
        for i in range(m,m+n):
            nums1[i]=nums2[k]
            k+=1
        nums1.sort()
        
