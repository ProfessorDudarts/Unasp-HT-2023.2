def contador_vogais(texto: str):
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0

    for letra in texto.lower():
        if letra in vogais:
            contador += 1
    
    return contador

total = contador_vogais('Eduardo Mendes')
print(f'Total = {total}')

