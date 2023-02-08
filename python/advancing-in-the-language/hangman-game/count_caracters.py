total = 0
word = "python3"
finished = False

while not finished:
    finished = (total == len(word)) # retorna true of false
    total = total + 1

print(total - 1)

# List Comprehension 

inteiros = [1,3,4,5,7,8,9]
pares = [ x for x in inteiros if x % 2 == 0 ]
# o if depois do for que define a condição!

#quadrado de inteiros 
inteiros2 = [1,3,4,5,7,8]
quadrado = [ n*n for n in inteiros2 ]
print(quadrado)