import random
# Diferentemente das funções built-in, o módulo random precisa ser explicitamente importado no seu programa.

random_number = round(random.random() * 100) # int cortar todos os decimais
print(random_number)

# A função random.randrange() quando só possuí um parâmetro supõe que você quer dizer de zero até número passado -1,