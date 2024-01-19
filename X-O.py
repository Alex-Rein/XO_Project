import random

turn_count = 0
field = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]


def greetings():  # Приветствие и правила игры
    print("""Приветствую в игре крестики нолики!
Правила игры просты:
1. Главная цель - первым собрать линию из трёх своих символов в строке, столбце или диагонали.
2. Крестики и нолики делают свой ход по очереди.
3. Ход выполняется указанием номера столбца(X) и номера строки(Y) куда хотите сходить.
4. На занятую оппонентом клетку делать ход нельзя.
""")
    input("Нажмите Enter чтобы начать")


def turn():  # Объявление игрока + счетчик хода (глобальный)
    global turn_count
    turn_count += 1
    if turn_count < 10:
        print("Ходят крестики!") if turn_count % 2 == 0 else print("Ходят нолики!")


def random_start():  # Случайно определяем кто ходит первым
    global turn_count
    check = random.randrange(10)
    print(check)
    if check < 5:  # Ходят крестики, иначе нолики
        turn_count += 1


def draw_field():  # Отрисовка игрового поля (с координатами на В и Л границах)
    print("\n"*3)
    print("  0 1 2")
    for i in range(3):
        print(str(i), *field[i])
    print()


def player_symbol():  # Позвращает символ игрока
    return "x" if turn_count % 2 == 0 else "o"


def move():  # Укороченная функция хода по координатам с проверками
    while True:  # Цикл проверки правильности хода
        while True:  # Тут получаем и проверяем сразу обе координаты
            coords = input("Введите X и Y через пробел: ").split()
            if len(coords) == 2 and all(map(str.isdigit, coords)):
                if int(coords[0]) in range(3) and int(coords[1]) in range(3):
                    x, y = int(coords[0]), int(coords[1])
                    break
                else:
                    print("Координаты вне поля игры! Укажите значения от 0 до 2")
            else:
                print("Указаны неправильные координаты!")
        if field[y][x] == "-":  # Проверка доступности хода
            field[y][x] = player_symbol()  # Делаем ход
            break
        else:  # Все фигня, давай по новой
            print("Клетка занята, укажите свободную!")


def win_check():  # Проверка на выигрыш сходившего игрока
    c = player_symbol()
    check_result = False

    for row in field:  # Проверка горизонтальных линий
        cnt = 0
        for i in range(3):
            cnt += row[i] == c
        check_result = cnt == 3
        if check_result:
            break

    if not check_result:  # Проверка вертикальных линий
        for i in range(3):
            cnt = 0
            for row in field:
                cnt += row[i] == c
            check_result = cnt == 3
            if check_result:
                break

    if not check_result:
        cnt = 0
        for i in range(3):  # Проверка первой диагонали
            cnt += field[i][i] == c
        check_result = cnt == 3

    if not check_result:
        cnt = 0
        for i in range(3):  # Проверка второй диагонали
            j = 2 - i
            cnt += field[i][j] == c
        check_result = cnt == 3

    return check_result


def winner():  # Объявление победителя
    player = "Крестики" if turn_count % 2 == 0 else "Нолики"
    print(f"Поздравляю! {player} победили!")


def draw():  # Обработка ничьей
    if turn_count == 10:
        print("Получилась ничья! Вы сильные соперники!")
        return True


def start_game():  # Функция запуска игры
    greetings()
    random_start()
    draw_field()
    while True:
        turn()
        if draw():
            break
        move()
        draw_field()
        if win_check():
            winner()
            break


start_game()  # Let's begin the massacre! >:)
