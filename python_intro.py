def hi(imie):
    if imie == 'Ola':
        print('Hej Ola!')
    elif imie == 'Sonja':
        print('Hej Sonja!')
    else:
        print('Hej nieznajoma!')
dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
def hi(imie):
    print('Witaj ' + imie + '!')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
    hi(imie)
    print('Kolejna dziewczyna')
for i in range(1, 6):
    print(i)
