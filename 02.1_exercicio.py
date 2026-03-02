num_1 = int (input("Digite um número inteiro: "))
num_2 = int (input("Digite mais um número inteiro: "))
num_3 = int (input("Digite o último número inteiro: "))

if num_1 > num_2 and num_1 > num_3:
    print (f"{num_1} é maior que {num_2} e {num_3}.")

elif num_2 > num_1 and num_2 > num_3:
    print (f"{num_2} é maior que {num_1} e {num_3}.")

elif num_3 > num_1 and num_3 > num_2:
    print (f"{num_3} é maior que {num_1} e {num_2}.")

else: 
    print ("Há números iguais ou não existe um maior.")