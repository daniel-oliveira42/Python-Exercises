ano_at = 2020

nas = int(input('Qual o seu ano de nascimento? '))
idade = ano_at - nas

if idade == 18:
    print('Está na hora de se alistar!')
elif idade > 18:
    print('Passara(m)-se {} ano(s) da hora de se alistar'.format(idade-18))
else:
    print('Falta(m) {} ano(s) para você precisar se alistar'.format(18-idade))

