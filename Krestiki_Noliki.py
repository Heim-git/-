import random


def console_print(field):
    count = 0
    print()
    for value in field:
        print("|", end=" ")
        print(value, end=" | ")
        count += 1
        if count % 3 == 0:
            print()
    print()


def player(field):
    move = input("Введите число:")
    if move in field:
        return move


def ii(field):
    while True:
        move = random.choice(field)
        for i in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            if i == move:
                return move


def check_winner(field):
    lines = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [1, 4, 7],
             [2, 5, 8],
             [3, 6, 9],
             [1, 5, 9],
             [3, 5, 7]
             ]
    for line in lines:
        symbols = []
        for row in line:
            symbol = field[row - 1]
            symbols.append(symbol)
        if symbols == ["X", "X", "X"]:
            return "X"
        elif symbols == ["0", "0", "0"]:
            return "0"
    return None


def logic():
    field = [str(i) for i in range(1, 10)]
    console_print(field)
    count2 = 0
    while True:
        count2 += 1
        new = player(field)
        b = int(field.index(new))
        field[b] = "X"
        console_print(field)
        winner = check_winner(field)
        if winner == "X":
            print("Победил игрок!!!")
            break
        elif winner == "0":
            print("Победил ИИ!!!")
            break
        elif count2 == 5:
            print("Ничья!!!")
            break
        new2 = ii(field)
        d = int(field.index(new2))
        field[d] = "0"
        console_print(field)
        winner = check_winner(field)
        if winner == "X":
            print("Победил игрок!!!")
            break
        elif winner == "0":
            print("Победил ИИ!!!")
            break
        elif count2 == 5:
            print("Ничья!!!")
            break
        else:
            continue


def main():
    logic()


if __name__ == '__main__':
    main()
