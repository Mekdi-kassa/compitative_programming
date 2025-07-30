class Solution {
  bool judgeSquareSum(int c) {
    int a = 0;
    int b = 0;
    double j = sqrt(c);
    int x = 0;
    for(int i = 0; i < j.toInt() + 1; i++){
        a = i * i;
        b = c - a;
        x = sqrt(b).toInt();
        if (( x * x) == b){
            return true;
        }
    }
    return false;
  }
}