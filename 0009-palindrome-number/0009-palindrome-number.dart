class Solution {
  bool isPalindrome(int x) {
    String n= x.toString();
    int left = 0;
    int right = n.length -1;
    while (left < right){
        if (n[left] != n[right]){
            return false;
        }
        left += 1;
        right -= 1;
    }
    return true;
  }
}