class Cat:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        return '!!!Cat object!!!'

    def get_name(self):
        print(self.name)

    def deposit(self, total, what=""):
        self.ledger.append({"amount": total, "description": what})

    def withdraw(self, amount, description=""):
#        x = self.get_balance(description)
#        print('withdraw ', x)
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
# dict.items() to get key and value pairs
    def get_balance(self, category=''):
        balance = 0
        for dict in self.ledger:
            balance = balance + dict["amount"]
        return balance

    def transfer(self, amount, description):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, "Transfer to " + description)
            self.deposit(amount, "Transfer from " + self.name)
            return True

    def check_funds(self, amount):
        # x = self.get_balance()
        if amount > self.get_balance():
            return False
        else:
            return True

# ledger is list of dictionary with key, val descripton and amount
# x = Cat("food")
# x.get_name()
# print(x.__dict__)


def create_spend_chart(categories=[]):
    #return bar chart string
    return "bar chart"

y = Cat('Tommy')

y.get_name()

y.deposit(5, "cats")
y.deposit(45, "berries")
y.deposit(5, 'berries')
y.withdraw(5, 'berries')
print(y.__dict__)
print(y.get_balance('berries'))
print(y.get_balance('cats'))
print(y.__dict__)
print(y.check_funds(15))
print(y)
