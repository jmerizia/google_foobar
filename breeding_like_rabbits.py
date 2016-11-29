# Breeding Like Rabbits

# The idea here will be to recursively call R(n)
# in order to get values of R from values. This makes
# the computation time generally shorter, because
# not all points in the series are calculated and it
# happens in reverse. It also takes advantage of
# Python's ability to remember long chains of recursive
# function calls, so instead of saving the whole
# instruction in a dict, only the values can be
# cached/saved.
# The answer() function will take the base-10 input
# and run a simple midpoint binary search from the
# array of odds, then evens if it isn't caught. If
# a value is found, it is returned. If it isn't
# caught by either search, the function returns None.

series = {0:1, 1:1, 2:2}

def potato(n):
    if n in series:
        return series[n]
    elif n % 2 == 0: # n is even
        num = n / 2
        series[n] = potato(num) + potato(num + 1) + num
    elif n % 2 != 0: # n is odd
        num = (n - 1)/ 2
        series[n] = potato(num) + potato(num - 1) + 1
    return series[n]

def answer(str_S):
    
    k = int(str_S)

    if k == 1 or k == 0:
        return 1

    # 1 is odd, 0 is even
    for parity in [1, 0]:

        # change first & last based on parity
        first = 0 + parity
        last = (k >> 1) * 2 + parity + 4
        
        while last - first > 2:

            midpoint = (first + last) / 2

            if parity == 1 and midpoint % 2 == 0:
                midpoint += 1
            if parity == 0 and midpoint % 2 != 0:
                midpoint += 1

            value = potato(midpoint)

            if value == k:
                return midpoint
            else:
                if k < value:
                    last = midpoint
                else:
                    first = midpoint

# NOTE: I know not adding/subtracting 1 from
# the endpoints upon reiteration is unconventional.
# I just kept getting annoying infinite loop
# bugs writing it conventionally. This approach
# doesn't sacrifice too much computation time
# anyways :P
