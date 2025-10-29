class ATM:

    def __init__(self):
        self.dict1 = defaultdict(int)
        
    def deposit(self, banknotesCount: List[int]) -> None:
        self.dict1[20] += banknotesCount[0]
        self.dict1[50] += banknotesCount[1]
        self.dict1[100] += banknotesCount[2]
        self.dict1[200] += banknotesCount[3]
        self.dict1[500] += banknotesCount[4]
        
    def withdraw(self, amount: int) -> List[int]:
        temp_dict = self.dict1.copy()
        num = amount
        ans = [0] * 5
        
        
        if num >= 500 and temp_dict[500] > 0:
            n = min(num // 500, temp_dict[500])  
            num -= n * 500
            temp_dict[500] -= n
            ans[4] = n
        
  
        if num >= 200 and temp_dict[200] > 0:
            n = min(num // 200, temp_dict[200])
            num -= n * 200
            temp_dict[200] -= n
            ans[3] = n
        

        if num >= 100 and temp_dict[100] > 0:
            n = min(num // 100, temp_dict[100])
            num -= n * 100
            temp_dict[100] -= n
            ans[2] = n
        

        if num >= 50 and temp_dict[50] > 0:
            n = min(num // 50, temp_dict[50])
            num -= n * 50
            temp_dict[50] -= n
            ans[1] = n
        

        if num >= 20 and temp_dict[20] > 0:
            n = min(num // 20, temp_dict[20])
            num -= n * 20
            temp_dict[20] -= n
            ans[0] = n
        

        if num != 0:
            return [-1]
 
        self.dict1 = temp_dict
        return ans