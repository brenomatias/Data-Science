class Account:

    def __init__(self, number, holder, balance, limit):
        self.__numero = number
        self.__titular = holder
        self.__saldo = balance
        self.__limite = limit
    
    def extract(self):
        print("Seu saldo {}".format(self.__saldo))

    def deposit(self, value):
        self.__saldo += value

    def __can_withdraw(self, value):
        avaible_credit = self.__saldo + self.__limite
        return value <= avaible_credit

    def withdraw(self, value):
        if(self.__can_withdraw(value)):
            self.__saldo -= value
        else:
            print("The value {} exceed the limit".format(value))
    
    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)
    
    @property
    def balance(self):
        return self.__saldo
    
    @property
    def holder(self):
        return self.__titular
    
    @property
    def limit(self):
        return self.__limite
    
    @limit.setter
    def limit(self, limit):
        self.__limite = limit

    @staticmethod
    def bank_code():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

# para tornar um objeto privado, adiciona dois caracteres underscore (__)
# Com o uso do return, sempre nos será retornado o valor de um atributo
# 'getters' ( nos dão um dado)
#  'setters' ( modificam os dados) Lembrem-se que com set nunca retornaremos um valor, nós iremos modificar um atributo

# Importante: Usem os getters e setters com parcimônia. Eles devem ser criados apenas quando forem necessários.

# métodos estaticos: Nosso foco está nos métodos estáticos que são da classe, e mesmo sem o objeto, conseguimos executar o método
# Quando todos os objetos compartilham algo em comum, faz sentido usar esses métodos — como no exemplo em que compartilhamos todos os códigos do banco (metodo estatico nao precisa de iniciar um objeto para ser acessado)