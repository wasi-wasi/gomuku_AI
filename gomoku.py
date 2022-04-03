"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

''' Assigned Coded Functions '''

def is_empty(board):
    '''Returns true if the board is empty.'''
    # NOTE: To call this function you have to call  make_empty_board(sz) first.

    a = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                a = a+1
    if len(board)*len(board[0]) == a:
        return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    ''' Return the state of the given sequence. '''

    x_start = 0
    y_start = 0

    # (1,0)
    if d_y == 1 and d_x == 0:
        # Find y_start & x_start
        x_start = x_end
        y_start = y_end - length + 1
        # Semi-Open Case:
        if y_start == 0 and y_end == 7:
            return "CLOSED"
        if y_start == 0:
            if board[y_end + 1][x_end] ==  " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end == 7:
            if board[y_start - 1][x_start] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        # Open Case:
        if board[y_end + 1][x_end] == " " and board[y_start - 1][x_start] == " ":
            return "OPEN"
        # Closed Case:
        if board[y_end + 1][x_end] != " " and board[y_start - 1][x_start] != " ":
            return "CLOSED"
        else:
            return "SEMIOPEN"

    # (0, 1)
    if d_y == 0 and d_x == 1:
        # Find y_start & x_start
        x_start = x_end - length + 1
        y_start = y_end
        # Semi-Open Case:
        if x_start == 0 and x_end == 7:
            return "CLOSED"
        if x_start == 0:
            if board[y_end][x_end + 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if x_end == 7:
            if board[y_start][x_start - 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        # Open Case:
        if board[y_end][x_end + 1] == " " and board[y_start][x_start - 1] == " ":
            return "OPEN"
        # Closed Case:
        if board[y_end][x_end + 1] != " " and board[y_start][x_start - 1] != " ":
            return "CLOSED"
        else:
            return "SEMIOPEN"


    # (1, 1)
    if d_y == 1 and d_x == 1:
        # Find y_start & x_start
        x_start = x_end - length + 1
        y_start = y_end - length + 1
        # Edge Cases:
        if y_start == 0:
            if x_end != 7:
                if board[y_end + 1][x_end + 1] == " ":
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
        if y_start == 0 and x_start == 0 and y_end == 7 and x_end == 7:
            return "CLOSED"
        if (x_start == 0 and y_end == 7) or (x_end == 7 and y_start == 0):
            return "CLOSED"
        #Semi_open Case :
        if x_start == 0 or y_start == 0:
            if board[y_end + 1][x_end + 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if x_end == 7 or y_end == 7:
            if board[y_start - 1][x_start - 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        # Open Case:
        if board[y_start - 1][x_start - 1] == " " and board[y_end + 1][x_end + 1] == " ":
            return "OPEN"
        # Closed Case:
        if board[y_start - 1][x_start - 1] != " " and board[y_end + 1][x_end + 1] != " ":
            return "CLOSED"
        else:
            return "SEMIOPEN"

    # (1, -1)
    if d_y == 1 and d_x == -1:

        # Find y_start & x_start
        x_start = x_end + length - 1
        y_start = y_end - length + 1
        if y_end == 7 and x_end == 0:
            if x_start == 7 or y_start == 0:
                return "CLOSED"
            else :
                if board[y_start - 1][x_start + 1] == " ":
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
        elif y_end == 0 and x_end == 7:
            return "SEMIOPEN"
        elif x_end == 0 and y_end == 0:
            return "CLOSED"
        elif y_end == 7 and x_end == 7:
            return "CLOSED"
        elif x_end == 0 and y_start == 0:
            return "CLOSED"
        elif y_end == 7 and x_start == 7:
            return "CLOSED"
        elif x_end==0:
            if x_start == 0:
                return closed
            else:
                board[y_start - 1][x_start + 1] == " "
                return "SEMIOPEN"

        # Semi-Open Case:
        if y_end == 7:
            if x_start == 0:
                return closed
            else:
                board[y_start - 1][x_start + 1] == " "
                return "SEMIOPEN"
        elif x_start == 0 or y_start == 0:
            if x_end !=7 or y_end !=7 :
                if board[y_end + 1][x_end - 1] == " ":
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
            else:
                return "CLOSED"
        elif x_start == 7:
            if board[y_end + 1][x_end - 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"

        elif x_end == 7 and y_end != 7:
            if board[y_start - 1][x_start + 1] == " ":
                return "SEMIOPEN"
            else:
                return "CLOSED"
        # Open Case:
        elif board[y_start - 1][x_start + 1] == " " and board[y_end + 1][x_end - 1] == " ":
            return "OPEN"
        # Closed Case:
        elif board[y_start - 1][x_start + 1] != " " and board[y_end + 1][x_end - 1] != " ":
            return "CLOSED"
        else:
            return "SEMIOPEN"

def detect_row(board, col, y_start, x_start, length, d_y, d_x):

    open_seq_count = 0
    semi_open_seq_count = 0

    # Creating the tuple of open and semi-open sequences
    for a in range(length):
        if x_start >= 0 and x_start <= 7:
            if y_start >= 0 and y_start <=7:
                if board[y_start][x_start] == col:
                    # Calculate y_end and x_end
                    if d_y == 0 and d_x == 1:
                        y_end = y_start
                        x_end = x_start + length - 1
                    elif d_y == 1 and d_x == 0:
                        y_end = y_start + length - 1
                        x_end = x_start
                    elif d_y == 1 and d_x == 1:
                        y_end = y_start + length - 1
                        x_end = x_start + length - 1
                    elif d_y == 1 and d_x == -1:
                        y_end = y_start + length - 1
                        x_end = x_start - length - 1
                    if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN":
                        open_seq_count += 1
                    elif is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMIOPEN":
                        semi_open_seq_count += 1
                    else:
                        continue
                    # Calculate new y_start and x_start
                    if d_y == 0 and d_x == 1:
                        y_start = y_end
                        x_start = x_end + 2
                    elif d_y == 1 and d_x == 0:
                        y_start = y_end + 2
                        x_start = x_end
                    elif d_y == 1 and d_x == 1:
                        y_start = y_end + 2
                        x_start = x_end + 2
                    elif d_y == 1 and d_x == -1:
                        y_start = y_end + 2
                        x_start = x_end - 2
                else:
                    y_start += d_y
                    x_start += d_x
        else:
            break

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):

    open_seq_count, semi_open_seq_count = 0, 0
    track_count_open, track_count_semi_open = 0, 0
    track_count_open_1, track_count_semi_open_1 = 0, 0
    track_count_open_2, track_count_semi_open_2 = 0, 0
    track_count_open_3, track_count_semi_open_3 = 0, 0

    d_y = 1
    d_x = 0
    y_start = 0
    x_start = 0
    for x_start in range(8):
        open_count, semi_open_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        track_count_open += open_count
        track_count_semi_open += semi_open_count

    d_y = 0
    d_x = 1
    y_start = 0
    x_start = 0
    for y_start in range(len(board)):
        open_count, semi_open_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        track_count_open_1 += open_count
        track_count_semi_open_1 += semi_open_count

    d_y = 1
    d_x = 1
    y_start = 0
    x_start = 0
    for x_start in range(len(board)):
        y_start += 1
        open_count, semi_open_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        track_count_open_2 += open_count
        track_count_semi_open_2 += semi_open_count


    d_y = 1
    d_x = -1
    y_start = 0
    x_start = 0
    for x_start in range(len(board), -1):
        y_start += 1
        open_count, semi_open_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)
        track_count_open_3 += open_count
        track_count_semi_open_3 += semi_open_count

    track_open = track_count_open + track_count_open_1 + track_count_open_2 + track_count_open_3
    track_semi_open = track_count_semi_open + track_count_semi_open_1 + track_count_semi_open_2 + track_count_semi_open_3

    return track_open, track_semi_open

def search_max(board):
    for i in range(len(board)):
        for j in range(len(board)):
            a = board[i][j]
            if board[i][j] == " ":
                board[i][j] = "b"
                if is_win(board) == "Black won":
                    board[i][j] = a
                    return (i,j)
                else:
                    board[i][j] = a
    h= board
    I = []
    for i in range(8):
        for j in range(8):
            h[i][j] = board[i][j]
            if board[i][j] == " ":
                board[i][j] = "b"
                I.append(score(board))
                board[i][j] == h[i][j]
    x = argmin(I)
    m = x//(len(board))
    c = x%(len(board))

    return (m,c)

def is_win(board):

    if is_full(board) == True:
        return "Draw"

    col ="b"
    count = 0
    for i in reversed(range(len(board))):
        for j in range(len(board)):
            if board[i][j] == col:
                if board[i - 1][j] == col:
                    if board[i - 2][j] == col:
                        if board[i - 3][j] == col:
                            if board[i - 4][j] == col:
                                count = 1
                            if board[i - 5][j] == col:
                                count = 0
            if count == 1:
                return "Black won"



    count = 0
    for j in range(len(board)):
        for i in range(len(board)):
            if board[i][j] == col:
                if board[i][j - 1] == col:
                    if board[i][j - 2] == col:
                        if board[i][j - 3] == col:
                            if board[i][j - 4] == col:
                                count = 1
                            if board[i][j - 5] == col:
                                count = 0
            if count == 1:
                return "Black won"


    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == col:
                if board[i - 1][j - 1] == col:
                    if board[i - 2][j - 2] == col:
                        if board[i - 3][j - 3] == col:
                            if board[i - 4][j - 4] == col:
                               count = 1
                            if board[i - 5][j - 5] == col:
                                count = 0
            if count == 1:
                return "Black won"

    count = 0
    for i in range(len(board)):
        for j in range(len(board) - 2):
            if board[i][j] == col:
                if board[i - 1][j + 1] == col:
                    if board[i - 2][j + 2] == col:
                        if board[i - 3][j + 3] == col:
                            if board[i - 4][j + 4] == col:
                                count = 1
                            if board[i - 5][j + 5] == col:
                                count = 0
            if count == 1:
                return "Black won"

    col ="w"
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == col:
                if board[i - 1][j] == col:
                    if board[i - 2][j] == col:
                        if board[i - 3][j] == col:
                            if board[i - 4][j] == col:
                                count = 1
                            if board[i - 5][j] == col:
                                count = 0
            if count == 1:
                return "White won"


    count = 0
    for j in range(len(board)):
        for i in range(len(board)):
            if board[i][j] == col:
                if board[i][j - 1] == col:
                    if board[i][j - 2] == col:
                        if board[i][j - 3] == col:
                            if board[i][j - 4] == col:
                                count = 1
                            if board[i][j - 5] == col:
                                count = 0
            if count == 1:
                return "White won"


    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == col:
                if board[i - 1][j - 1] == col:
                    if board[i - 2][j - 2] == col:
                        if board[i - 3][j - 3] == col:
                            if board[i - 4][j - 4] == col:
                                count = 1
                            if board[i - 5][j - 5] == col:
                                count = 0
            if count == 1:
                return "White won"


    for i in range(len(board)):
        for j in range(len(board) - 2):
            if board[i][j] == col:
                if board[i - 1][j + 1] == col:
                    if board[i - 2][j + 2] == col:
                        if board[i - 3][j + 3] == col:
                            if board[i - 4][j + 4] == col:
                                count = 1
                            if board[i - 5][j + 5] == col:
                                count = 0
            if count == 1:
                return "White won"

    if is_full(board) != True:
        return " Continue Playing"
    else:
        return"Draw"

''' Helper Functions '''

def is_full(board):
    '''Returns true if the board is full.'''
    # NOTE: To call this function you have to call  make_empty_board(sz) first.
    a = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != ' ':
                a = a+1
    if len(board)*len(board[0]) == a:
        return True

'''Given Base Functions'''

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))



def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

''' Modified Test Functions '''

def test_is_empty():
    board  = make_empty_board(8)
    put_seq_on_board(board, 1, 4, 1, 0, 2, "b")
    print_board(board)
    if is_empty(board) == True:
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():

    # Test 1 : Open

    board = make_empty_board(8)
    x = 4; y = 1; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 2

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN":
        print("TEST CASE 1 for is_bounded PASSED ")
    else:
        print("TEST CASE 1 for is_bounded FAILED")

    # Test 2 : Semi-open
    board = make_empty_board(8)
    x = 4; y = 4; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 7
    x_end = 1

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE 2 for is_bounded PASSED ")
    else:
        print("TEST CASE 2 for is_bounded FAILED")

    # Test 3 : Closed
    board = make_empty_board(8)
    x = 3; y = 0; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 0

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 3 for is_bounded PASSED ")
    else:
        print("TEST CASE 3 for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 7; y = 0; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    print(detect_row(board, "w", y, x, length, d_y, d_x))

# def test_detect_row():
#     board = make_empty_board(8)
#     x = 5; y = 1; d_x = 0; d_y = 1; length = 3
#     put_seq_on_board(board, y, x, d_y, d_x, length, "w")
#     print_board(board)
#     if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
#         print("TEST CASE for detect_row PASSED")
#     else:
#         print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 1; y = 1; d_x = 1; d_y = 0; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    print(detect_rows(board, col, length))

def test_search_max():
    board = make_empty_board(8)
    x = 1; y = 0; d_x = 1; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 2; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    print(search_max(board) == (4,6))

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | | | | *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | |w"| | | | *
    #           4 | | | |w| | | *
    #           5 | | | | |b| | *
    #           6 | | | | | | | *
    #           7 | | | | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':

    '''Testing Individual Functions'''
    # test_is_empty()
    # test_is_bounded()
    test_detect_row()
    #test_detect_rows()
    # test_search_max()

    ''' Testing is win '''
    # board = make_empty_board(8)
    # print_board(board)
    # put_seq_on_board(board, 0, 1, 1, 0, 8, "b")
    # put_seq_on_board(board, 0, 2, 1, 0, 8, "b")
    # put_seq_on_board(board, 0, 3, 1, 0, 8, "b")
    # put_seq_on_board(board, 0, 4, 1, 0, 8, "b")
    # put_seq_on_board(board, 0, 5, 1, 0, 8, "b")
    # put_seq_on_board(board, 0, 6, 1, 0, 8, "b")
    # put_seq_on_board(board, 0, 7, 1, 0, 8, "b")
    # put_seq_on_board(board, 0, 0, 1, 0, 8, "b")
    # put_seq_on_board(board, 1, 1, 0, 1, 8, "w")
    # put_seq_on_board(board, 2, 2, 1, 1, 1, "b")
    # put_seq_on_board(board, 2, 3, 0, 1, 2, "w")
    # put_seq_on_board(board, 0, 7, 1, 0, 3, "b")
    # put_seq_on_board(board, 0, 0, 1, 1, 2, "w")
    # put_seq_on_board(board, 7, 0, 0, 1, 6, "b")
    # put_seq_on_board(board, 3, 2, 1, 1, 5, "w")
    # put_seq_on_board(board, 0, 1, 0, 1, 4, "b")
    # put_seq_on_board(board, 0, 5, 0, 1, 2, "w")
    # print_board(board)
    # print(is_win(board))

