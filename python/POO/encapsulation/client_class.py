class Client:

    def __init__(self, name):
        self.__nome = name
    
    @property
    def nome(self):
        print("Calling @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, name):
        print("Calling setter nome()")
        self.__nome = name

# A declaração de uma property é feita com o uso do caractere @
# o objetivo é que a execução ocorra, mesmo sem os parênteses. 'object.method.()'
# os METODOS QUE DÃO ACESSO são nomeados como 'properties'
# Com @property, indicamos que estamos trabalhando com uma propriedade.
# '.title()' garante que o nome vai começar com maisculo