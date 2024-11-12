Cores = {'Azul': {'escuro', 'claro'}, 'Amarelo': {'queimado', 'neon'}, 'marrom': 'sim'}

print(Cores)
azul = Cores.get('Azul')
azul_escuro = Cores.get(['Azul']['escuro'])
print(azul)
print(azul_escuro)