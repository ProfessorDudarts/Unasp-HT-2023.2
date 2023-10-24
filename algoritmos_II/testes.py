import unittest

# A função que você deseja testar
def calcular_media(numeros):
    if not numeros:
        return 0
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

def test_media_lista_vazia():
    assert calcular_media([]) == 0

def test_media_lista_um_elemento():
    assert calcular_media([5]) == 5.0
    print('ok')

def test_media_lista_multiplos_elementos():
    assert calcular_media([1, 2, 3, 4, 5]) == 3.0

if __name__ == '__main__':
    test_media_lista_vazia()
    test_media_lista_um_elemento()
    test_media_lista_multiplos_elementos()