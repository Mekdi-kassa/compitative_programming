class Solution {
  int searchInsert(List<int> nums, int target) {
    int high = nums.length ;
    int low = 0;
    int mid = 0;
    while (low < high){
        mid = (high + low)~/2;
        if(nums[mid] ==  target){
            return mid;
        }
        else if (nums[mid] < target){
            low = mid + 1;
        }
        else{
            high = mid;
        }
    }
    return low;
  }
}