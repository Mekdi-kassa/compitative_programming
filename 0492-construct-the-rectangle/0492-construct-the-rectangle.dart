class Solution {
  List<int> constructRectangle(int area) {
    List<List<int>> matrix = [];
    for(int i = 1 ; i < sqrt(area).toInt() + 1; i++){
        if(area % i == 0){
            matrix.add([i,area~/i,(i - area~/i).abs()]);
        }
    }
    matrix.sort((a, b) => a[2].compareTo(b[2]));
    return [matrix[0][1], matrix[0][0]];

  }
}