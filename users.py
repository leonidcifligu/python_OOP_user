class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
 
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def make_transfer(self,user,amount):
        self.account_balance-= amount
        user.account_balance+= amount

user1 = User("User 1", "user@gmail.com")
user2 = User("User 2", "user2@gmail.com")
user3 = User("User 3", "user3@gmail.com")

user1.make_deposit(1)
user1.make_deposit(4)
user1.make_deposit(7)
user1.make_withdrawl(7)


user2.make_deposit(2)
user2.make_deposit(7)
user2.make_withdrawl(2)
user2.make_withdrawl(3)

print(user2.account_balance)

user1.make_transfer(user2,3)
print(user1.account_balance,user2.account_balance)
print(user2.account_balance)
