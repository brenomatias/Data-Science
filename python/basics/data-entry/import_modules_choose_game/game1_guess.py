import random

def play_guess():
    secret_number = round(random.randrange(1, 101))#.random.random() gera número entre 0.0 e 1.0 inicialmente
    hits_number = 0
    points = 1000

    print("Qaul o nível de dificuldae?")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    # for variable in range(1, 10):
    # range(start, stop[, step]) ->  'step' value controls the increment between the values in the range
    nivel = int(input("Define o nível: "))

    if nivel == 1:
        hits_number = 20
    elif nivel == 2:
        hits_number = 10
    else:
        hits_number = 5

    for round in range(1, hits_number + 1):
        print("Try {} of {}".format(round, hits_number))
        guess = input("Type a number: ")
        guess_number = int(guess)
        print("You typed", guess_number)

        if guess_number < 1 or guess_number > 100:
            print("You must type a number between 1 and 100")
            continue #nao sai do laço, apenas da iteração especifica (pula para proxima iteraçao)

        right = guess_number == secret_number
        lower = guess_number < secret_number
        higher = guess_number > secret_number

        if right:
            print("Voce acertou e fez {} pontos".format(points))
            break #parar e sair do laço
        else: 
            if lower:
                print("Voce errou. O numero e maior que", guess_number)
            elif higher:
                print("Voce errou. O número é menor que", guess_number)
            lost_points = abs(secret_number - guess_number) #  retornar o número desconsiderando o seu sinal
            points = points - lost_points

    print("end game, o numero secreto é {} e seu número de pontos é {}".format(secret_number, points))

if(__name__ == "__main__"): #executar direto pelo python3 -> so para chamar diretamente
    play_guess()
# (__name__ == "__main__") define chamar a função apenas ne execução direta pelo 'python3'