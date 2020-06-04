pic = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
sperator = "-"
order = 0
over = False

def create_table(pic, sperator):
    print(sperator * 9)
    for i in range(3):
        print("|", " ".join(pic[i]), "|")
    print(sperator * 9)

def count(alist):
    x = 0
    o = 0
    for i in alist:
        x += i.count("X")
        o += i.count("O")
    return x, o

def win_or_not(pic):
    ang_rh = ""
    ang_lt = ""
    for i in range(3):
        hor_line = ""
        ver_line = ""
        for j in range(3):
            hor_line += pic[i][j]
            ver_line += pic[j][i]
            if i == j:
                ang_rh += pic[i][j]
            elif abs(i - j) == 2:
                ang_lt += pic[i][j]
        if hor_line == "XXX" or ver_line == "XXX":
            return "X wins"
        elif hor_line == "OOO" or ver_line == "OOO":
            return "O wins"
    ang_lt += pic[1][1]
    if ang_lt == "XXX" or ang_rh == "XXX":
        return "X wins"
    elif ang_rh == "OOO" or ang_lt == "000":
        return "O wins"
    else:
        return False

def determine_wf(pic):
    x, o = count(pic)
    if x + o == 9 and not win_or_not(pic):
        return "Draw"
    elif x + o < 9 and not win_or_not(pic):
        pass
    else:
        return win_or_not(pic)

def convert_cor(move):
    b = move[0] - 1
    if move[1] == 1:
        a = 2
    elif move[1] == 2:
        a = 1
    else:
        a = 0
    return a, b

def play(pic, sperator):
    global order
    avail_move = False
    while not avail_move:
        try:
            move = input("Enter the coordinates: ").split()
            move = [int(i) for i in move]
            if move[0] > 3 or move[1] > 3:
                print("Coordinates should be from 1 to 3!")
            else:
                a, b = convert_cor(move)
                if pic[a][b] != " ":
                    print("This cell is occupied! Choose another one!")
                else:
                    if order % 2 == 0:
                        pic[a][b] = "X"
                    else:
                        pic[a][b] = "O"
                    order += 1
                    avail_move = True
        except ValueError:
            print("You should enter numbers!")
    create_table(pic, sperator)

create_table(pic, sperator)
while not over:
    play(pic, sperator)
    if determine_wf(pic):
        over = True
        print(determine_wf(pic))







