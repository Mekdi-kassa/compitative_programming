class Solution {
  int singleNumber(List<int> nums) {
    Map<int,int> m = {};
    for (int i = 0; i< nums.length ; i++){
        int key = nums[i];
        m[key] = (m[key] ?? 0) + 1;
    }
    for (var x in m.entries) {
        if (x.value == 1){
            return x.key;
        }
    }
    return -1;
  }
}