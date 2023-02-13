def create_account(numero, titular, saldo, limite):
    account = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return account

def deposit(account, value):
    account["saldo"] += value

def withdraw(account, value):
    account["saldo"] -= value

def extract(account):
    print("You have {} in your account".format(account["saldo"]))

# objetivo é criar uma classe para agrupar as informações e métodos do objeto