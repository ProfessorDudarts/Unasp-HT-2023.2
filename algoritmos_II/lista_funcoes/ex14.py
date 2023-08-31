def quadrado(**kwargs) -> None:
    base = kwargs['base']
    altura = kwargs['altura']
    print('* ' * base)
    for _ in range(altura - 2):
        print(f'* {"  " * (base - 2)}* ')
    print('* ' * base)



quadrado(altura=8, base=10)    