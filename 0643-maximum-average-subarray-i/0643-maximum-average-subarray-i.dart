class Solution {
  double findMaxAverage(List<int> nums, int k) {
    if (nums.isEmpty || k <= 0 || k > nums.length) return 0.0;
  
    int maxSum = 0;
    for (int i = 0; i < k; i++) {
      maxSum += nums[i];
    }
    
    int currentSum = maxSum;
    
    for (int i = k; i < nums.length; i++) {
      currentSum = currentSum - nums[i - k] + nums[i];
      if (currentSum > maxSum) {
        maxSum = currentSum;
      }
    }
    
    return maxSum / k;
  }
}