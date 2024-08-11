print("Welcome to XO Game")
name = input("Enter your name ")

var_num = 0
l = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def checknum(a, b):
    global var_num
    if str(a) in l:
        tempin = l.index(str(a))
        l[tempin] = b
        var_num += 1
        return True
    else:
        print("Invalid input")
        return False

def checkwin_row():
    for i in range(3):
        if l[i * 3] == l[i * 3 + 1] == l[i * 3 + 2]:
            if l[i * 3] in "Xx":
                print("X won")
                return True
            else:
                print("O won")
                return True
    return False

def checkwin_column():
    for i in range(3):
        if l[i] == l[i + 3] == l[i + 6]:
            if l[i] in "Xx":
                print("X won")
                return True
            else:
                print("O won")
                return True
    return False

def checkwin_diagonal():
    if l[0] == l[4] == l[8]:
        if l[0] in "Xx":
            print("X won")
            return True
        else:
            print("O won")
            return True
    if l[2] == l[4] == l[6]:
        if l[2] in "Xx":
            print("X won")
            return True
        else:
            print("O won")
            return True
    return False

def print_board():
    print(f" {l[0]} | {l[1]} | {l[2]} ")
    print("---|---|---")
    print(f" {l[3]} | {l[4]} | {l[5]} ")
    print("---|---|---")
    print(f" {l[6]} | {l[7]} | {l[8]} ")

print_board()

while True:
    ini = input("Enter the starting symbol (X or O): ").upper()
    if ini in ["X", "O"]:
        break
    else:
        print("Type either X or O")

if ini == "X":
    var = ["X","O","X","O","X","O","X","O","X"]
else:
    var = ["O","X","O","X","O","X","O","X","O"]

while True:
    print_board()
    print(f"Position for {var[var_num]}: ")
    posin = int(input(""))
    if not checknum(posin, var[var_num]):
        continue
    
    if checkwin_row() or checkwin_column() or checkwin_diagonal():
        break
    
    if var_num >= 9:
        print("Tied")
        break

print_board()
print(f"{name}, you have completed XO")
