from account_class import Account
from client_class import Client

account1 = Account(123, "Nico", 3, 3000)
account2 = Account(23, "Joao", 100, 1000)
# account1.saldo 
# Não podemos acessar o atributo saldo do objeto diretamente. Teremos que usar os métodos responsáveis por encapsular o acesso ao objeto.

account1.transfer(10, account2)
account1.extract()
account2.extract()

#account1.set_limit(1000)
#print(account1.get_limit())

account1.limit = 10
# execução do método, agora sem '()' -> setter usando @property
# parece que que acessa o objeto diretamente, mas é um setter
print(account1.limit)

print(account1.balance)
print(account1.withdraw(100))

client = Client("breno")
print(client)
