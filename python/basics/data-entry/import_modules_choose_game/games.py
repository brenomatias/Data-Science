def choose_game():   
    print("Choose your game")
    import game1_guess as guess
    import game2_forca as forca
    # modulos que são definidos em função nao sao executados diretamente (se a fun nao for chamada no mesmo modulo)
    # importa e executa os módulos diretamente (isso se o módulo importado não for uma func definida)
    # se a função for chamada no fim do módulo, ela e executada também

    print("(1) Forca, (2) Advinhação")
    game = int(input("Qual o jogo? "))
    print(game)

    if game == 1:
        print("Jogando forca")
        forca.play_forca()
    elif game == 2:
        print("Jogando advinhação")
        guess.play_guess()

#  if que garante a execução como programa principal:
if __name__ == "__main___": # para que seja possível chamar o arquivo diretamente do terminal? (independene dos outros módulos)
    choose_game()
