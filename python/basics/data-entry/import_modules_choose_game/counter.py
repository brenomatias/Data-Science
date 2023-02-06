counter = 1
while counter <= 10:
    print(counter)
    counter = counter + 2
    if(counter == 5):
        counter = counter + 2

# Ambos, if e while, possuem uma condição de entrada. A diferença é que o if executa o bloco apenas uma vez, mas o while repete o bloco enquanto a condição for verdadeira.

# O interessante é que o Python não possui um laço com uma condição de saída, que outras linguagens chamam de do-while.