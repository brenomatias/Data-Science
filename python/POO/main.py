from teste import create_account

numero = 123
titular = "Nico"
saldo = 55.0
limite = 1000.0

# POO tem como foco a representação de objetos e suas funcionalidades e atributos
#  dicionário - chave: valor
conta = {"numero": 123, "titular": "Nico", "saldo": 55.5, "limite": 1000.0}
conta2 = {"numero": 321, "titular": "Jose", "saldo": 100, "limite": 2000}
# A melhor solução será definirmos uma função que encapsule esse código

account = create_account(123, "Breno", 55.0, 1000)
print(account["titular"])