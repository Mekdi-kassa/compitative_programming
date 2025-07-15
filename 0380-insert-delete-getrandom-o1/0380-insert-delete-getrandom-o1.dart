class RandomizedSet {
  Set<int> arr = {};
  RandomizedSet() {
    
   }
 
  bool insert(int val) {
    if(arr.contains(val)){
        return false;
    }
    else{
        arr.add(val);
        return true;
    }
  }
  
  bool remove(int val) {
    if(!arr.contains(val)){
        return false;
    }
    else{
        arr.remove(val);
        return true;
    }
  }
  
  int getRandom() {
    return arr.elementAt(Random().nextInt(arr.length));
  }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = RandomizedSet();
 * bool param1 = obj.insert(val);
 * bool param2 = obj.remove(val);
 * int param3 = obj.getRandom();
 */