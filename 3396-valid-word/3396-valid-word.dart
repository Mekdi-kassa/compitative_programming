class Solution {
  bool isValid(String word) {
    int n = word.length;
    if (n < 3){
        return false;
    }
    Set <String> s = {'a','e','i','o','u'};
    Set <String> nu = {'1','2','3','4','5','6','7','8','9','0'};
    int countv = 0;
    int countc = 0;
    bool numb = false;
    for (int i = 0; i < n;  i++){
        if (RegExp(r'^[a-zA-Z]$').hasMatch(word[i])){
            if(s.contains(word[i].toLowerCase())){
                countv ++;
            }
            else{
                countc ++;
            }
        }
        else if (nu.contains(word[i])){
            numb = true;
        }
        else{
            return false;
        }

    }
    if (countc > 0 && countv > 0){
        return true;
    }
    return false;
  }
}