# break

# imie = "Hermenegilda"
#
# for litera in imie:
#     if litera == 'n':
#         break
#     print(litera)
#
# print("koniec")

# imie2 = "Agnieszka"

# for litera1, litera2 in zip(imie, imie2):
#     print(litera1, litera2)


indeksy = '012345678911'
zdanie = 'Ala ma kota kot ma ale'

for i, l in zip(indeksy, zdanie):
    print(i, l)