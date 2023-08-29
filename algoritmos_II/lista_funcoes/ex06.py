def encontrar_primos(numero: int):
    primos = []
    for i in range(1, numero + 1):
        if e_primo(i):
            primos.append(i)
            print(i)
    
    return primos


def e_primo(numero):
    for i in range(2, numero):
        divide = numero % i == 0
        if divide:
            return False
        
    return True

lista_primos = encontrar_primos(154346574)
print(lista_primos)

if __name__ == "__main__":
    import cProfile
    cProfile.run("encontrar_primos(154344)")