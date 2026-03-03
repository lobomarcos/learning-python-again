a = float (input("Digite o primeiro lado do triângulo: "))
b = float (input("Digite o segundo lado do triângulo: "))
c = float (input("Digite o último lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c: 
        print ("Triângulo equilátero.")
    elif a == b or a == c or b == c:
        print ("Triângulo isósceles.")
    else:
        print ("Triângulo escaleno.")
else:
    print ("Não é um triângulo.")