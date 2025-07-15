class Solution {
  bool isValid(String s) {
    var set1={')':'(','}':'{',']':'['};
    List<String> arr = [];
    int n = s.length;; 
    for (int i = 0; i < n; i++){
        if (set1.containsKey(s[i])){
            if (arr.isNotEmpty && set1[s[i]] == arr.last) {
                arr.removeLast();
            } else {
                return false;
            }
        }
        else{
            arr.add(s[i]);
        }
        
    }
    return arr.isEmpty;
  }
}