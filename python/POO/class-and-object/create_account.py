# antes de criarmos um objeto definiremos uma classe.
# criaremos um objeto, no caso, falamos de uma conta, algo concreto
# antes de termos um objeto, devemos definir as suas características.

class Account():

    def __init__(self, number, holder, balance, limit):
        print("Construindo objeto")
        self.numero = number
        self.titular = holder
        self.saldo = balance
        self.limite = limit




# Python pode executar uma função, automaticamente, dentro da classe para definir os atributos (__init__). Construtor inicia os atributos da classe (função construtora)

#Criamos uma função, mas a ideia é definir os atributos e as características. Para isso, precisaremos da variável self

#self é a referência que sabe encontrar o objeto construído em memória.