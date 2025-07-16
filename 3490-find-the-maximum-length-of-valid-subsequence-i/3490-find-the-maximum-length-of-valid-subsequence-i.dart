import 'dart:math';
class Solution {
  int maximumLength(List<int> nums) {
    int even = 0;
    int odd = 0;
    int alt = 1;
    int prev = nums[0];
    if (prev % 2 == 0){
        even ++ ;
    }
    else{
        odd ++;
    }
    for (int i = 1; i < nums.length ; i++){
        if(prev % 2 != nums[i] % 2){
            alt += 1;
            prev = nums[i];
        }
        if (nums[i] % 2 == 0){
            even ++;
        }
        else{
            odd ++;
        }
    }
    return max(odd , max(even ,alt));
  }
}