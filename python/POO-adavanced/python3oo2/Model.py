from collections.abc import MutableSequence

class TV_Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0
      
    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f'{self._name} - {self.year} - {self._likes} Likes'

class Film(TV_Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year) 
        self.duration = duration
    
    def __str__(self):
        return f'{self.name} - {self.year} - {self.duration} min - {self.likes} Likes'
    
    def return_custom_register():
        pass

class Serie(TV_Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons
    
    def __str__(self):
        return f'{self.name} - {self.year} - {self.seasons} seasons - {self.likes}'

class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs
    
    @property
    def size(self):
        return len(self._programs)
    
    def __getitem__(self, item):
        return self._programs[item]
    
    def __len__(self):
        return len(self._programs)

vingadores = Film('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Film('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.give_like()
atlanta.give_like()
tmep.give_like()
tmep.give_like()
demolidor.give_like()

films_and_series = [vingadores, atlanta, tmep, demolidor]
weekend_playlist = Playlist('Weekend', films_and_series)

print(f'Playlist lenght: {len(weekend_playlist)}')

for program in weekend_playlist:
   print(program)
# aqui acontece o polimorfismo. Nao importa qual e a classe do programa

print(f'Does it has? {demolidor in weekend_playlist}')
print(weekend_playlist[1])


















# Normalmente usamos o init para definir os atributos, mas o que fazer se precisarmos definir um valor padrão para todos os objetos? Ou até criar um atributo que será compartilhado para todas as instâncias?

# Para isto, vai ser necessário criar um atributo ligado à classe, ao invés de ligado à instância (self).

class Person:
    cpf_size = 11

    def __init__(self, cpf, name):
        self.cpf = cpf
        self.name = name
    
    def validate_cpf(self):
        return True if len(self.cpf) == __class__.cpf_len else False
    
# este atributo vai ser modificado ao longo do tempo, e nao na incializaçao
# def give_like(self):
#self.__likes += 1
    

## Atributo privado '__' não vai para a classe filha
# 'super' extende a super class (classe mae)

# o super(), que por sua vez chama qualquer método ou atributo da classe mãe

# 'super().__init__()' incializa a clase mae
# '__str__' representaçao textual de objetos
#__getitem__(), que indica ao Python que a classe poderia ser usada para um for in, ou um in [LISTA INTERNA]
# Deste modo, sempre que o len() externo for chamado, conseguiremos obter o __len__() da nossa listagem interna