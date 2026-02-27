frase = str(input("Digite a frase para saber quantas letras ela tem: "))

tamanho = len(frase) - frase.count(" ")

print("O tamanho da frase é de: {} letras." .format(tamanho))