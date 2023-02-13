from account_model import create_account, deposit, withdraw, extract

account = create_account(123, "Nico", 55.0, 1000.0)
deposit(account, 15.0)
extract(account)

withdraw(account, 20)
extract(account)

print(account["saldo"])