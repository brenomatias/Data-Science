import random

def start_message():
    print("*************")
    print("Welcome to the game")
    print("************")

def load_secret_word():
    words_file = open("words.txt")
    avaible_words = []

    for line in words_file:
        line = line.strip()
        avaible_words.append(line)

    words_file.close()
    random_number = random.randrange(0, len(avaible_words))
    secret_word_open = avaible_words[random_number].upper()

    return secret_word_open

def hit_letter(word):
    return ["_" for letra in word]

def ask_guess():
    guess = input("What is the word?")
    guess = guess.strip().upper()
    return guess

def play():
    start_message()
    
    secret_word = load_secret_word()
    hits_letter_hits = hit_letter(secret_word)

    hanged = False
    hit = False
    erros = 0

    print(hits_letter_hits)

    while (not hanged and not hit):
       
        guess_letter = ask_guess()

        if(guess_letter in secret_word):
            index = 0
            for letter in secret_word:
                if (guess_letter == letter):
                    hits_letter_hits[index] = letter
                index += 1
        else:
            erros += 1
            print("Você erro! Faltam {} tentativas".format(6-erros))

        hanged = erros == 6
        hit = "_" not in hits_letter_hits # nao existe underscore na lista de chutes
        print(hits_letter_hits)
            
    if(hit):
        print("You won!")
    else:
        print("You lost")

    print("End of game")

if(__name__ == "__main__"):
    play()

#.find()
# iterar em cima de cada letra -> 'for': usado para sequencias
# A palavra é uma sequência de letras, logo podemos utilizar o laço for
# a iteração vai passar por cada letra [0, 1, 3, 4, 5, 6]. 
# a cada iteração o index aumenta, se a letra existir, printa, se nao so continua a iteraçao
# list [] -> sequencia de valores
# randrange, que recebe o intervalo de valores que o número aleatório deve estar.
# Então vamos passar o valor 0 (equivalente à primeira posição da nossa lista) e 4 (lembrando que o número é exclusivo, ou seja, o número aleatório será entre 0 e 3, equivalente à última posição da nossa lista)a
# random.range(0,4)