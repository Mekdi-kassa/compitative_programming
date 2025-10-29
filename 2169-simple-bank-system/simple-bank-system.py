class Bank:

    def __init__(self, balance: List[int]):
        self.banks = balance
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0 <= account1 - 1 < len(self.banks) and 0 <= account2 - 1 < len(self.banks):
            if self.banks[account1 - 1] - money >= 0:
                self.banks[account1 - 1] -= money
                self.banks[account2 - 1] += money
                return True
        return False
    def deposit(self, account: int, money: int) -> bool:
        if 0 <= account - 1 < len(self.banks):
            self.banks[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 <= account - 1 < len(self.banks):
            if self.banks[account - 1] - money >= 0:
                self.banks[account - 1] -= money
                return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)