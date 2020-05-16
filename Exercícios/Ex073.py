times = \
    ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
     'Fortaleza EC', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro',
     'CSA', 'Chapecoense', 'Avaí')
print(f'Os 5 times na liderança são: {times[:5]}')
print(f'Os 4 lanternas são: {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está em {times.index("Chapecoense")+1}° lugar')