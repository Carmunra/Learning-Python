altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em Kg: "))

imc = peso / altura**2

print("Seu IMC é: %.4f" % imc)

if imc < 16:
    print("Magraze grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obseidade Grau III (mórbida)")