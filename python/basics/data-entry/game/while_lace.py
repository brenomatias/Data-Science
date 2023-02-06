print("Bem vindo ao jogo!")
print("\n")

secret_number = 43
total_guess = 3
round = 1

while round <= total_guess:
    print("tetantiva {} de {}".format(round, total_guess))
    guess_str = input("Digite o seu número: ")
    guess_number = int(guess_str)
    print("voce digitou", guess_number)

    hit = guess_number == secret_number #True or False
    higher_hit = guess_number > secret_number
    lower_hit = guess_number < secret_number

    if hit:
        print("voce acertou.")
    else:
        if higher_hit:
            print("voce chutou pra cima")
        elif lower_hit:
            print("voce chutou para baixo")
    round = round +1

print("End of game")
# para indicar o início do bloco if, é necessário utilizar dois pontos (:)
# Quando usamos apenas um =, estamos atribuindo um valor à variável. Para compararmos valores ou variáveis, usamos o ==.