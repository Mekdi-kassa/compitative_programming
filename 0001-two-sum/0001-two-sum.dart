class Solution {
  List<int> twoSum(List<int> nums, int target) {
    for(int i = 0; i < nums.length  ;i++ ){
        for (int j = i + 1 ; j < nums.length ; j++){
            int sum1 = nums[i] + nums[j];
            if (sum1 == target){
                return [i , j];
            }
        }
       
    }
    return [];

  }
}