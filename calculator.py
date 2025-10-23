import math

print('================== \n Area Calculator 📐 \n==================')
print('\n 1) Triangle \n 2) Rectangle \n 3) Square  \n 4) Circle  \n 5) Quit \n')

shape = int(input('Select shape: '))

area = 0

if shape == 1:
    h = int(input('Height: '))
    b = int(input('Base: '))
    area = (h * b) / 2
    print(f'The area is: {area}')
elif shape == 2:
    l = int(input('Length: '))
    w = int(input('Width: '))
    area = l * w
    print(f'The area is: {area}')
elif shape == 3:
    s = int(input('Side: '))
    area = s ** 2
    print(f'The area is: {area}')
elif shape == 4:
    r = int(input('Radius: '))
    area = math.pi * (r ** 2)
    print(f'The area is: {area}')
elif shape == 5:
    print('You are quitting calculator! \n You may leave this terminal. Have a good day!')