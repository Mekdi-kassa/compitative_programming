class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dict1 = defaultdict(SortedList)
        self.food_info = {}
        n = len(foods)
        for i in range(n):
            self.food_info[foods[i]] = (cuisines[i],ratings[i])
            self.dict1[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        if food not in self.food_info:
            return 
        old_cuisine, old_rating = self.food_info[food]
        
        # Remove old entry from cuisine map
        self.dict1[old_cuisine].remove((-old_rating, food))
        
        # Update food info
        self.food_info[food] = (old_cuisine, newRating)
        
        # Add new entry to cuisine map
        self.dict1[old_cuisine].add((-newRating, food))
    def highestRated(self, cuisine: str) -> str:
        return self.dict1[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)