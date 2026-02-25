opt = str (input("A temperatura para conversão está em Fahrenheit ou Celsius? [C / F] "))

if opt in "Cc":
    celsius = float (input("Digite a temperatura para converter para Fahrenheit: "))
    f = celsius * 1.8 + 32
    print ("A temperatura de {}° Celsius em Fahrenheit é: {}° F." .format(celsius, f))

elif opt in "Ff":
    fahrenheit = float (input("Digite a temperatura para converter para Celsius: "))
    c = (fahrenheit - 32)/ 1.8
    print ("A temperatura de {}° Fahrenheit em Celsius é {}° C." .format(fahrenheit, c))

else:
    print ("Opção inválida. Digite apenas C ou F.")