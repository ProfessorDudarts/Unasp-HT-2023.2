def media(nota1: int, nota2: int, peso1: int  = 1, peso2: int = 1):
    media_final = (nota1 * peso1 + nota2 * peso2)/(peso1 + peso2)
    return media_final


print(media(8, 7))
print(media(8, 7, 3, 4))
print(media(7, 8, 3, 4))
print(media(peso1=6, nota2=9, peso2=2, nota1=10))