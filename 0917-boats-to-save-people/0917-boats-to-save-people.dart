class Solution {
  int numRescueBoats(List<int> people, int limit) {
    people.sort();
    int right =people.length - 1;
    int left = 0;
    int count = 0;
    while (left <= right){
        if (people[left] + people[right] <= limit){
            left ++;
        }
        right --;
        count += 1;
    }
    return count;
  }
}