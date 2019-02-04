class Bank:

    account={'balance':0}
    def account_balance(self):
        #import pdb;pdb.set_trace()
        return self.account
    def minimum_balance(self,minbal):
        self.minbal=minbal

    def deposit(self,amount):
        self.account['balance']+=amount
    def withdraw(self,amount):
        #import pdb;pdb.set_trace()
        if self.account['balance']-amount<self.minbal:
            return "Cannot withraw ,maintain minimum balance"
        else:
            self.account['balance']-=amount


cust1=Bank()
cust1.minimum_balance(50000)
print(cust1.account_balance())
cust1.deposit(150000)
print(cust1.account_balance())
cust1.withdraw(50000)
cust1.withdraw(50000)
print(cust1.account_balance())
print(cust1.withdraw(50000))