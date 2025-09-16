class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        amount = floor((purchaseAmount + 5)/10) * 10 
        return 100 -amount



        