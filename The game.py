def greet():
    print("-----------------\n"
          "Приветствуем Вас\n"
          "     в игре     \n"
          "крестики - нолики\n"
          "-----------------\n"
          "Формат ввода: x y\n"
          "x - номер строки\n"
          "y - номер столбца")


def show():
    print()
    print("   | 0 | 1 | 2 |")
    print(" ---------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" ---------------")
    print()


def ask():

    while True:
        cords = input("       Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите две координаты!")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 and y < 0 or y > 2:
            print("Координаты вне диапазона!")
            continue
        if field[x][y] != " ":
            print("Клетка занята!")
            continue
        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            show()
            print("Выиграл X !!!")
            return True
        if symbols == ["O", "O", "O"]:
            show()
            print("Выиграл O !!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    a, b = ask()
    if num % 2 == 1:
        field[a][b] = "X"
    else:
        field[a][b] = "O"
    if check_win():
        break
    if num == 9:
        show()
        print("Ничья")
        break
