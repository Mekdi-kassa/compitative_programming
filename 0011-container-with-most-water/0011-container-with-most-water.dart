class Solution {
  int maxArea(List<int> height) {
    int area = 0;
    int left = 0;
    int right = height.length - 1;
    int width = 0;
    int minheight = 0;

    while (left <= right){
        minheight = min(height[left], height[right]);
        width = right - left;
        area = max(area,(minheight * width));
        if (height[left] < height[right]){
            left += 1;
        }
        else{
            right -= 1;
        }
    }
    return area;


  }
}