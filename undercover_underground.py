# Undercover Underground

# This problem was very tricky, since the highest
# math class I have ever taken was linear algebra.
# The first thing I noticed is that the when
# n == k - 1 is true, it is equal to n^(n - 2), or
# Cayley's Formula (A000272).
# After some more research and playing with numbers,
# I stumbled on A123527, a fairly recent entry. It
# uses the triangle number series to find the total
# possibilities of graphs. I had to fix an error in
# Geoffrey Critzer's formula however. I had to take
# into account the number of graphs that have
# unconnected vertices and remove them from the
# total. Finding a function that evaluated this
# difference was undoubtably the hardest part...
# I just figured out a way from looking at the
# series.
# Then, I eventually had to add memoising for
# efficiency

from math import factorial

binoms = {}
def binom(n, k): # simple "n choose k" function
    if (n, k) in binoms:
        return binoms[(n, k)]
    if n - k < 0: # just in case
        binoms[(n, k)] = 0
    else:
        binoms[(n, k)] = factorial(n) / (factorial(n - k) * factorial(k))
    return binoms[(n, k)]

posss = {}
def poss(n, k): # from A123527, determines max combinations
    if (n, k) in posss:
        return posss[(n, k)]
    else:
        posss[(n, k)] = binom(binom(n, 2), k)
    return posss[(n, k)]

answers = {}
def answer(n, k):
    if (n, k) in answers:
        return answers[(n, k)]
    if k >= binom(n - 1, 2) + 1:
        answers[(n, k)] = poss(n, k)
    else:
        value = poss(n, k)

        for x in range(0, n - 1):
            b = min((x + 1) * x >> 1, k)
            for y in range(x, b + 1):

                # recursively find answer(a + 1, b)
                # this made sense after I took a look
                # at the factorization of each term of 
                # the list of differences
                difference_partial = answer(x + 1, y) * binom(n - 1, x) * poss(n - x - 1, k - y)
                value -= difference_partial
        answers[(n, k)] = value
    return answers[(n, k)]

print answer(7, 20), answer(7, 7), answer(6, 6), answer(9, 15)