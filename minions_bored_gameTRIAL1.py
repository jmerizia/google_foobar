# Minions Bored Game (TRIAL)

def answer(t, n):

    # The goal here would be to code a
    # simple turing machine. Then, with the
    # help of the turing machine and some
    # study, a function can be designed
    # that more specifically and efficiently
    # solves the problem.

    # initiate starting position:
    game = [0]


    for roll in range(t):
        next_game = []
        #print game
        for position in game:
            if position == 0:
                next_game.extend([0,1])

            elif position == n - 1:
                next_game.extend([position])

            else:
                next_game.extend([position - 1, position, position + 1])

        game = next_game

    return game.count(n - 1)



for n in range(2, 10):
    final = ""
    for t in range(1, 13):
        ans = str(answer(t, n))
        final = final + " "*(5 - len(ans)) + ans
    print final + "\n"