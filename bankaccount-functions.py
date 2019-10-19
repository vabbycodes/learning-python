class Bankaccount(object):
    def __init__(self, initbalance):
        self.balance=initbalance
    def deposit (self, amount):
        self.balance= self.balance+amount

    def withdraw(self, amount):
        self.balance= self.balance - amount

    def getbalance(self):
        return self.balance


firstaccount = Bankaccount(500)
secondaccount = Bankaccount(1000)

firstaccount.deposit(100)
secondaccount.withdraw(100)

print(firstaccount.getbalance())
print(secondaccount.getbalance())


    
