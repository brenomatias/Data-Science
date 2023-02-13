from create_account import Account

# Account()

# Se quisermos trabalhar com o objeto, temos que chamaremos a classe Conta, guardando o retorno dentro de uma varíavel de referência. Esta referência guardará o endereço em memória para localizar o objeto posteriormente

# test_account = Account() 
# endereço não é o objeto em si. Trata-se apenas de uma referência.

account1 = Account(223, "Test", 44.0, 1000.0)
account2 = Account(233, "Pedro", 30, 500)

print(account1.saldo)
print(account2.titular)