# Breeding Like Rabbits (TRIAL)

def answer(str_S):

    n = 5

    offset = 10

    a = 60
    b = 13
    print a.format(10), b.format(10)

    quit()

    #n += offset

    series = [1, 1, 2, 3]
    series = [22, 12, 25, 18]

    possible = []
    counter = 0

    if int(str_S) == 1:
        return 1
    if int(str_S) == 2:
        return 2
    if int(str_S) == 3:
        return 3

    while n < int(str_S) + int(str_S) / 10:
        print "Find >", n
        if n % 2 != 0: # it's odd
            thing = (n - 1) / 2
            val = series[thing] + series[thing - 1] + 1
            if val == int(str_S):
                possible.append(n)
            series.extend(['.', val])
            n -= 1
        else: # it's even
            thing = n / 2
            other_thing = (n + offset) / 2
            val = series[thing] + series[thing + 1] + other_thing
            if val == int(str_S):
                possible.append(n)
            series[n] = val
            n += 3
        print series
        if len(possible) > 0:
            counter += 1
        if counter == 10:
            return possible[-1]


num = 10 ** 3 + 2

print answer("12")