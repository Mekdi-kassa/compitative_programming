class Solution {
  List<int> twoSum(List<int> nums, int target) {
    int n = nums.length;
    for (int i = 0;i <n;i++){
        for (int j = i + 1; j < n ;j ++){
            if (nums[i] + nums[j] == target){
                return [i,j];
            }
        }
    }
    return [];
  }
}