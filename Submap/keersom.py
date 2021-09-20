getal = input('met welke getal wil je de x som weten? ')
print('dit is de tafel van', getal)

getal = int(getal)
for teller in range(1,11):
    print(teller, 'x', getal, '=', teller * getal)
print()