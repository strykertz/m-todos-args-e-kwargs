################### Função ARGS ####################

# Parâmetros args é utilizada em momentos que não sabemos quantos parametros queremos passar.

def teste(arg, *args):
    print(f'primeiro argumento normal: {arg}')
    for arg in args:
        print(f'outro argumento: {arg} ')


teste('python', 'é', 'do', 'caralho', 'puta que pariu!')

print(' ')

################## Função KWARGS ###################
print(' ')

# Função kwargs tem a mesma premissa do args, porém ele passa dicionário com argumentos nomeados.


def minha_função(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))


minha_função(nome='marcus')

dicionário = {'nome': 'marcus', 'idade': 27}
minha_função(**dicionário)
