def check_3(a, b, c):
    return a == b == c and a != "_"


def check_c(n):
    if not n.isdigit():
        print("You should enter numbers!")
        return False
    elif int(n) < 1 or int(n) > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    else:
        return True


def check_f(x, y, field):
    if field[3 - int(y)][int(x) - 1] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    return True


def prf(field):
    print("---------")
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(field[i][j] + " ", end="")
        print("|")
    print("---------")


def wnr(field):
    for i in range(3):
        if check_3(field[i][0], field[i][1], field[i][2]) or check_3(field[0][i], field[1][i], field[2][i]):
            return True
    if check_3(field[0][0], field[1][1], field[2][2]) or check_3(field[0][2], field[1][1], field[2][0]):
        return True
    return False

s = "_________"
field = [list(s[0:3]), list(s[3:6]), list(s[6:9])]
prf(field)
tg = "X"

for _ in range(9):
    ok_inp = False
    while not ok_inp:
        x, y = input("Enter coordinates:").split()
        ok_inp = check_c(x) and check_c(y) and check_f(x, y, field)
    field[3 - int(y)][int(x) - 1] = tg
    prf(field)
    if wnr(field):
        print(tg, "wins")
        break
    if tg == "X":
        tg = "O"
    else:
        tg = "X"
else:
    print("Draw")