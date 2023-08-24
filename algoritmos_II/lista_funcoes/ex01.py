import math

def maior_numero_com_max(lista_numeros):
    maior = max(lista_numeros)
    return maior

def maior_numero(lista_numeros):
    maior = -math.inf
    for item in lista_numeros:
        if maior < item:
            maior = item
    
    return maior

lista = [-3,-6,-17,-8,-9, 8, 8,9,0]
maior = maior_numero(lista)
maior = maior_numero_com_max(lista)
print(f'Maior = {maior}')

if __name__ == "__main__":
    import cProfile
    cProfile.run("maior_numero_com_max(lista)")
    cProfile.run("maior_numero(lista)")
