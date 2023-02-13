from class_contructor import Account

account1 = Account(123, "Pedro", 33, 140)
account1 = Account(123, "Pedro", 33, 140)

another_ref = account1 #funciona como uma cópia, aponta para o mesmo objeto

#O que acontece se quisermos desfazer uma referência, por exemplo, desreferenciar outraRef? Para isto, podemos usar a palavra especial None:
another_ref = None