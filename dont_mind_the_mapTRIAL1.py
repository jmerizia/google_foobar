# Don't Mind the Map (TRIAL)

import itertools

def removeStation(subway, n):
    new_subway = subway[:]
    # close station n
    new_subway[n] = "closed"
    # reroute other stations
    for k in range(len(new_subway)):
        if k is not "closed":
            for line in range(len(new_subway[k])):
                if new_subway[k][line] == n:
                    if subway[n][line] == n:
                        new_subway[k][line] = k
                    else:
                        new_subway[k][line] = subway[n][line]
    return new_subway

def traversePath(subway, order):
    endpoints = []

    for k in range(len(subway)):
        # start at k
        station = k
        for line in order:
            if subway[station] is not "closed":
                station = subway[station][line]
            #print subway, order, station
            endpoints.append(station)
    return endpoints

def possibleOrders(subway, n):
    orders = []
    # create list with every line index
    num_lines = len(subway[n - 1])
    numbers = range(0, num_lines)

    for order in itertools.product(numbers, repeat=num_lines):
        orders.append(list(order))
    return orders

def answer(subway):
    orders = possibleOrders(subway, 0)
    for order in orders:
        endpoints = traversePath(subway, order)
        if len(list(set(endpoints))) == 1:
            return -1

    for k in range(0, len(subway)):
        new_subway = removeStation(subway, k)
        print new_subway
        for order in orders:
            endpoints = traversePath(new_subway, order)
            if len(list(set(endpoints))) == 1:
                return k

    return -2


subway = [[0, 1, 2, 3, 4, 5], [2, 0, 4, 1, 3, 4], [1, 1, 5, 1, 3, 4], [3, 5, 4, 1, 1, 2], [0, 4, 1, 3, 0, 5], [5, 5, 5, 5, 5, 1]]
#subway = [[0, 0, 0, 1, 2], [1, 1, 1, 2, 2], [2, 1, 2, 0, 0]]
#subway = [[0, 1, 2], [0, 1, 2], [2, 0, 1]]
#subway = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
#subway = [[2, 1], [2, 0], [3, 1], [1, 0]]
#subway = [[1, 2], [1, 1], [2, 2]]
#subway = [[3, 3, 3, 3], [3, 3, 3, 3], [3, 1, 3, 3], [3, 3, 3, 3]]
#subway = [[0], [0], [0], [0]]

print answer(subway)







