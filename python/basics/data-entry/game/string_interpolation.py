#DETALHES DE SINTAXE

print("try of {} from {}". format(3, 10))

print("try of {1} from {0}".format(3, 10)) # inverte a ordem dos parâmetros (0=3, 1=10)

# formatação ideal -> mostar pro python o tipo de dado que queremos receber 
# definir regras de formatação
print("R$ {:f}".format(1.59)) # f = tipo float

print("R$ {:.2f}".format(1.5)) # duas casa depois do ponto 

print("R$ {:7.2f}".format(1234.5)) # queremos receber 7 caracteres como total (incluindo o ponto) e duas casas depois do ponto
# 2f = numero com DUAS casas decimais
# 1f = numero com UMA casa decimal (pos ponto)

#preencher com 0 quando nao tem nada
print("R$ {:07.2f}".format(34.5)) # queremos trabalhar com 7 caracteres como total e duas casas depois do ponto (o '0' completa com 0 os numeros que nao tem os 7 caracteres totais)

print("R$ {:07d}".format(34)) # d = inteiro

print("Data {:02d}/{:02d}".format(10, 4)) # espera inteiros nas entradas. (.02 = exige dois numerais, e completa com 0 caso não tenha)