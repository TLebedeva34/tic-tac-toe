print("----------------------------------------")
print("Добро пожаловать в игру крестики-нолики!")
print("----------------------------------------")
print("Пожалуйста, пригласите друга, так как это парная игра!")
print("-----------------------------------------")
print("Выполняйте ходы по очереди.")
print("Введите 2 координаты для Вашего символа.")
print("Координаты обозначают строку и столбец соответственно.")
print("Числа должны быть от 0 до 2.")
print("-----------------------------------------")
print("Следуйте подсказкам, и всё получится!")
print("              Удачи!             ")


playing_field = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
def print_field():
    print("  0 1 2")
    print(f"0 {playing_field[0][0]} {playing_field[0][1]} {playing_field[0][2]}")
    print(f"1 {playing_field[1][0]} {playing_field[1][1]} {playing_field[1][2]}")
    print(f"2 {playing_field[2][0]} {playing_field[2][1]} {playing_field[2][2]}")

def request():
    while True:
        x, y = map(int, input("Куда будем ставить Ваш символ?").split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if playing_field[x][y] == "-":
                return x, y
            else:
                print("Место занято =( "
                      "Выберите другое!")
        else:
            print("Координаты вне диапазона =(")

request()

def chec_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for cord in win_cord:
        symbols = []

        for c in cord:
            symbols.append(playing_field[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
    return False

num = 0
while True:
    num += 1

    print_field()

    if num % 2 == 1:
        print("Поставьте крестика!")
    else:
        print("Теперь -  нолик! ")

    x, y = request()

    if num % 2 == 1:
        playing_field[x][y] = "X"
    else:
        playing_field[x][y] = "0"

    chec_win()

    if num == 9:
        break
        print("Ничья")

print_field()