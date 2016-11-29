# Minions Bored Game

def answer(t, n):

    # The goal here would be to code a
    # simple turing machine. Then, with the
    # help of the turing machine and some
    # study, a function can be designed
    # that more specifically and efficiently
    # solves the problem. Sadly, after several
    # hours of looking at the data chart, I
    # can't seem to find a small, elegant
    # two variable function. I do believe
    # one exists, and with more time I
    # could find one. But for now, the
    # below code functions properly. I have
    # pasted the data chart I have been
    # studying at the bottom.

    # establish the board to size...
    board = [1]
    for tile in range(n + 1):
        board.append(0)

    for roll in range(t):

        # create an empty board for future rounds...
        new_board = [0]
        for tile in range(n):
            new_board.append(0)

        # parse through each iteration of board
        for position in range(len(board)):
            if board[position] is not 0:
                if position is 0:
                    new_board[0] = new_board[0] + board[0]
                    new_board[1] = new_board[1] + board[0]

                elif position is n - 1:
                    new_board[n - 1] = new_board[n - 1] + board[n - 1]

                else:
                    new_board[position - 1] = new_board[position - 1] + board[position]
                    new_board[position] = new_board[position] + board[position]
                    new_board[position + 1] = new_board[position + 1] + board[position]

        board = new_board

    return board[n - 1] % 123454321


#                 DATA CHART:
#    1    2    3    4    5    6    7    8    9
#
#    0    1    3    7   15   31   63  127  255
#
#    0    0    1    4   12   32   81  200  488
#
#    0    0    0    1    5   18   56  162  450
#
#    0    0    0    0    1    6   25   88  283
#
#    0    0    0    0    0    1    7   33  129
#
#    0    0    0    0    0    0    1    8   42
#
#    0    0    0    0    0    0    0    1    9
#
#                  SOURCE:
#
#for n in range(2, 10):
#    final = ""
#    for t in range(1, 10):
#        ans = str(answer(t, n))
#        final = final + " "*(5 - len(ans)) + ans
#    print final + "\n"