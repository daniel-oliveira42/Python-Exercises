sexo = str(input('Insira seu sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválidos. Insira seu sexo novamente: ')).lower().strip()
if sexo == 'M':
    status = 'Masculino'
elif sexo == 'F':
    status = 'Feminino'

print('Você é do sexo {}'.format(status))

