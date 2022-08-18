import turtle
import time

windows = turtle.Screen()
windows.setup(800, 800)
windows.setworldcoordinates(-500, -500, 500, 500)
windows.title("Connect 4")
turtle.speed(0)
turtle.hideturtle()
windows.tracer(0)

score = turtle.Turtle()
score.up()
score.hideturtle()

rows = 6
cols = 7
start_x = -450
start_y = -450 * rows / cols
WIDTH = -2 * start_x
HEIGHT = -2 * start_y


def draw_rectangle(x, y, w, h, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()


def draw_circle(x, y, r, color):
    turtle.up()
    turtle.goto(x, y - r)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r, 360, 150)
    turtle.end_fill()


def draw_board():
    draw_rectangle(start_x, start_y, WIDTH, HEIGHT, 'light blue')


def draw_pieces():
    global board
    row_gap = HEIGHT / rows
    col_gap = WIDTH / cols
    Y = start_y + row_gap / 2

    for i in range(rows):
        X = start_x + col_gap / 2
        for j in range(cols):
            if board[i][j] == 0:
                draw_circle(X, Y, row_gap / 3, 'white')
            elif board[i][j] == 1:
                draw_circle(X, Y, row_gap / 3, 'black')
            else:
                draw_circle(X, Y, row_gap / 3, 'red')
            X += col_gap
        Y += row_gap


def draw():
    draw_board()
    draw_pieces()
    windows.update()


def game_over_lastmove(bb, turn, r, c):
    # check horizontals
    cnt = 1
    i = c + 1

    while i < cols and bb[r][i] == turn:
        cnt, i = cnt + 1, i + 1
    i = c - 1

    while i >= 0 and bb[r][i] == turn:
        cnt, i = cnt + 1, i - 1

    if cnt >= 4:
        return turn

    # check vertical
    if r >= 3 and bb[r - 1][c] == turn and bb[r - 2][c] == turn and bb[r - 3][c] == turn:
        return turn

    # check diagonal 1
    cnt = 1
    i = 1

    while r + i < rows and c + i < cols and bb[r + i][c + i] == turn:
        cnt, i = cnt + 1, i + 1
    i = -1

    while r + i >= 0 and c + i >= 0 and bb[r + i][c + i] == turn:
        cnt, i = cnt + 1, i - 1

    if cnt >= 4:
        return turn

    # check diagonal 2
    cnt = 1
    i = 1

    while r + i < rows and c - i >= 0 and bb[r + i][c - i] == turn:
        cnt, i = cnt + 1, i + 1
    i = -1

    while r + i >= 0 and c - i < cols and bb[r + i][c - i] == turn:
        cnt, i = cnt + 1, i - 1

    if cnt >= 4:
        return turn

    for i in range(cols):
        if bb[rows - 1][i] == 0:
            return -2
    return 0


# place piece in col for turn
def place_piece(bb, turn, col):
    for i in range(rows):
        if bb[i][col] == 0:
            bb[i][col] = turn
            return i


def init_board():
    global board
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        board.append(row)


def place_piece_and_draw(bb, turn, col):
    row = place_piece(bb, turn, col)
    row_gap = HEIGHT / rows
    col_gap = WIDTH / cols
    Y = start_y + row_gap * row + row_gap / 2
    X = start_x + col_gap * col + col_gap / 2
    i = row
    j = col
    if board[i][j] == 0:
        draw_circle(X, Y, row_gap / 3, 'white')
    elif board[i][j] == 1:
        for k in range(5):
            draw_circle(X, Y, row_gap / 3, 'white')
            windows.update()
            time.sleep(0.05)
            draw_circle(X, Y, row_gap / 3, 'black')
            windows.update()
            time.sleep(0.05)
    else:
        for k in range(5):
            draw_circle(X, Y, row_gap / 3, 'white')
            windows.update()
            time.sleep(0.05)
            draw_circle(X, Y, row_gap / 3, 'red')
            windows.update()
            time.sleep(0.05)
    return row


def play(x, y):
    global turn, working
    if working:
        return
    working = True
    cols = [900 / 7 * i - 450 + 900 / 14 for i in range(7)]
    for i in range(len(cols)):
        if abs(x - cols[i]) < 900 / 14 * 2 / 3 and board[rows - 1][i] == 0:
            rn = place_piece_and_draw(board, turn, i)
            r = game_over_lastmove(board, turn, rn, i)
            if r == 0:
                windows.textinput('Game over', 'tie')
            elif r == 1:
                windows.textinput('Game over', 'player 1 won')
            elif r == -1:
                windows.textinput('Game over', 'player 2 won')
            if r != -2:
                windows.bye()
            turn = -turn
    working = False


board = []
init_board()
draw_board()
draw_pieces()
turn = 1
working = False
windows.onclick(play)
windows.mainloop()