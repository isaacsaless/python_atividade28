# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
ano = datetime.datetime.now().year
maior = []
menor = []
nmenor = 0
nmaior = 0
print('Saiba quantas pessoas são maior e menor de idade dentro de uma lista.')
for i in range(0, 6):
    idade = int(input('Digite o ano de nascimento de uma pessoa: '))
    if ano - idade >=18:
        maior.append(idade)
        nmaior = len(maior)
    else:
        menor.append(idade)
        nmenor = len(menor)
print(f'Dentro da lista fornecida, existem {nmenor} pessoas menor de idade. E {nmaior} pessoas maior de idade')