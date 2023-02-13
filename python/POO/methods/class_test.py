from class_contructor import Account
from class_contructor import Date

account1 = Account(123, "Jose", 33, 1000.0)
account2 = Account(23, "Ze", 3, 100)

print(account1.extract())
print(account2.extract())

account1.deposit(200)
print(account1.saldo)

date = Date(21,11,2005)
print(date.print_date())