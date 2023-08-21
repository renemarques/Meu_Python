print('CALCULADORA IMC')
print('*'*20)


peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/(altura*altura)

if imc <= 18.5:
    print(f'O seu IMC é {imc:.1f}.\nVocê está abaixo do peso') 
elif imc <=24.9:
    print(f'O seu IMC é {imc:.1f}.\nDe acordo com seu IMC voce está no peso IDEAL')
elif imc <=29.9:
    print(f'O seu IMC é {imc:.1f}.\nDe acordo com seu IMC voce está Levemente acima do peso')
elif imc <=34.9:
    print(f'O seu IMC é {imc:.1f}.\nDe acordo com seu IMC voce está com Obesidade Grau I')
elif imc <=39.9:
    print(f'O seu IMC é {imc:.1f}.\nDe acordo com seu IMC voce está com Obesidade Grau II')
else :
    print(f'O seu IMC é {imc:.1f}.\nDe acordo com seu IMC voce está com Obesidade Morbida')