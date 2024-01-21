import random


def greetings():  # Приветствие и правила игры
    print("""Приветствую в игре крестики нолики!
Правила игры просты:
1. Главная цель - первым собрать линию из трёх своих символов в строке, столбце или диагонали.
2. Крестики и нолики делают свой ход по очереди.
3. Ход выполняется указанием номера столбца(X) и номера строки(Y) куда хотите сходить.
4. На занятую оппонентом клетку делать ход нельзя.
""")
    input("Нажмите Enter чтобы начать")


def turn(turn_count, first_player):  # Объявление игрока + счетчик хода
    turn_count += 1
    if turn_count < 10:  # Проверка что еще нет ничьей для вывода чей текущий ход
        if turn_count % 2 == 1:
            print('Ходят крестики') if first_player == 'x' else print('Ходят нолики')
        else:
            print('Ходят нолики') if first_player == 'x' else print('Ходят крестики')
    return turn_count


def random_start(turn_count):  # Случайно определяем кто ходит первым
    check = random.randrange(10)
    print(check)
    if check < 5:  # Ходят крестики, иначе нолики
        return "x"
    else:
        return "o"


def draw_field(field):  # Отрисовка игрового поля (с координатами на В и Л границах)
    print("\n"*3)
    print("  0 1 2")
    for i in range(3):
        print(str(i), *field[i])
    print()


def player_symbol(turn_count, first_player):  # Возвращает символ игрока
    if turn_count % 2 == 1:
        return 'x' if first_player == 'x' else 'o'
    else:
        return 'o' if first_player == 'x' else 'x'


def move(field, turn_count, first_player):  # Укороченная функция хода по координатам с проверками
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
            field[y][x] = player_symbol(turn_count, first_player)  # Делаем ход
            return field
        else:  # Все фигня, давай по новой
            print("Клетка занята, укажите свободную!")


def win_check(field, turn_count, first_player):  # Проверка на выигрыш сходившего игрока
    c = player_symbol(turn_count, first_player)
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


def winner(turn_count):  # Объявление победителя
    player = "Крестики" if turn_count % 2 == 0 else "Нолики"
    print(f"Поздравляю! {player} победили!")


def draw(turn_count):  # Обработка ничьей
    if turn_count == 10:
        print("Получилась ничья! Вы сильные соперники!")
        return True


def start_game():  # Функция запуска игры
    turn_count = 0  # Инициализация пекременных
    field = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    first_player = random_start(turn_count)

    greetings()
    draw_field(field)
    while True:
        turn_count = turn(turn_count, first_player)
        if draw(turn_count):
            break
        field = move(field, turn_count, first_player)
        print(turn_count, first_player)
        draw_field(field)
        if win_check(field, turn_count, first_player):
            winner(turn_count)
            break


start_game()  # Let's begin the massacre! >:)
