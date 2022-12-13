# Создайте программу для игры в ""Крестики-нолики"".

field = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def show_field():
    global field
    for i in range(0, len(field), 3):
        print(field[i], field[i+1], field[i+2])

show_field()

def find_number(num, list, symbol):
    for i in range(len(list)):
        if list[i] == num:
            list[i] = symbol
    show_field()

player1 = input('Имя первого игрока: ')
player2 = input('Имя второго игрока: ')

symbol1 = 'O'
symbol2 = 'X'

counter = 0
x1 = 0
x2 = 0
while counter < 9:
   if counter % 2 == 0:
    x1 = int(input(f'Ходит {player1}: '))
    find_number(x1, field, symbol1)
    counter += 1
   else:
    x2 = int(input(f'Ходит {player2}: '))
    find_number(x2, field, symbol2)
    counter += 1