from time import sleep
import os

red = '\u001b[41m'
white = '\u001b[47m'
black = '\u001b[40m'
RESET = '\u001b[0m'
pix = '   '


def draw_flag():
    width = 9
    height = 12
    offset = width // 2
    for i in range (height):
        if i == 0 or i == height - 1:
            print(f'{white}{pix * (4 + width)}{RESET}')
        else:
            print(f'{white}{pix * (2 + offset)}{red}{pix * (width - offset*2)}{white}{pix * (offset + 2)}{RESET}')
        if i + 1 < height // 2:
            offset -= 1
        elif i + 1> height // 2:
            offset += 1


def pattern(column):
    height = 9
    width = height
    offset = width // 2
    space = '   '
    for line in range (1, 1 + height):
        if line == height or line == 1:
            print(f'\u001b[{line};{column}H{space * offset}{white}{space}{RESET}{space * offset}')
        else:
            print(f'\u001b[{line};{column}H{space * offset}{white}{space}{RESET}{space * (height - offset * 2 - 2)}{white}{space}{RESET}{space * offset}')
        if line < (height + 1) // 2:
            offset -= 1
        else:
            offset += 1


def animation():
    colors = [45, 80, 105]
    height = 9
    width = height
    space = '   '
    for color in colors:
        os.system("cls")
        offset = width // 2
        for line in range(1, 1 + height):
            if line == height or line == 1:
                print(f'{space * offset}\u001b[48;5;{color}m{space}{RESET}{space * offset}')
            else:
                print(
                    f'{space * offset}\u001b[48;5;{color}m{space}{RESET}{space * (height - offset * 2 - 2)}\u001b[48;5;{color}m{space}{RESET}{space * offset}')
            if line < (height + 1) // 2:
                offset -= 1
            else:
                offset += 1
            sleep(0.5)
        print(f'\u001b[{height + 1}A') #поднять курсор


def sequence():
    file = open('sequence.txt')
    list_less = []
    list_more = []
    for line in file:
        item = float(line)
        if -5 < item < 0:
            list_more.append(item)
        if item < -5:
            list_less.append(item)
    file.close()
    len_less = len(list_less)
    len_more = len(list_more)
    print(f'{white}{' ' * len_less}{RESET} {round(len_less * 100 / (len_more + len_less), 2)}%')
    print(f'{red}{' ' * len_more}{RESET} {round(len_more * 100 / (len_more + len_less), 2)}%')


def func():
    for y in range (9, 1, -1): #три пробела - одинарный отступ по x
        print(f'{y}|{' ' * (y * 3 // 3 - 1)}/')
    print('1\u231E/' + '___'* 4)
    print('0   1   2   3')
func()


#draw_flag()

# numbers = 3
# for number in range (1, 1 + numbers*2):
#     pattern(number * 8 * 3)

#animation()
#sequence()
#func()

