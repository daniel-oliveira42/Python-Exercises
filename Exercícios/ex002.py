n1 = input("Valor a ser testado: ")

print(type(n1))
print('É alfanumérico? {}'.format(n1.isalnum()))
print('É alfabético? {}'.format(n1.isalpha()))
print('É ASCII? {}'.format(n1.isascii()))
print('É decimal? {}'.format(n1.isdecimal()))
print('É dígito? {}'.format(n1.isdigit()))
print('Pode usar como identificador? {}'.format(n1.isidentifier()))
print('Tá em minúsculo? {}'.format(n1.islower()))
print('É numérico? {}'.format(n1.isnumeric()))
print('Aparece em print? {}'.format(n1.isprintable()))
print('É só espaço? {}'.format(n1.isspace()))
print('É um título? {}'.format(n1.istitle()))
print('Tá em maiúsculo? {}'.format(n1.isupper()))


