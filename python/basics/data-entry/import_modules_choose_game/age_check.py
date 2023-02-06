age_str = input("Type your age: ")
age_int = int(age_str)

adult = age_int > 18
child = age_int < 12
teen = age_int >= 12

if adult:
    print("You are adult")
else: 
    if child:
        print("You are a child")
    elif teen:
        print("you are a teenager")

# a instrução else não aceita receber uma condição.

# código que não roda
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
else(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
else(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")

# código que roda:
usuario_dois = input("iforme o usuário: ")

if usuario_dois == "flávio":
    print("Seja bem vindo", usuario_dois)
elif usuario_dois == "douglas":
    print("seja bem vindo", usuario_dois)
elif usuario_dois == "Nico":
    print("seja bem vindo", usuario_dois)
else:
    print("usuário nao encontrado")

# deixamos apenas um else que não recebe qualquer condição