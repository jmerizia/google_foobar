# Don't Mind the Map (TRIAL)

from itertools import product
from copy import deepcopy

# i.e. order = [0, 1] (based on number of lines per station)
# "k" is index for station
# "station" is the vector for station

def traversePath(subway, order):
    endpoints = []
    # start at each station once
    for k in range(len(subway)):
        # traverse through the stations using order
        next_station = k
        for index in order:
            next_station = subway[next_station][index]
        endpoints.append(next_station)
    if len(list(set(endpoints))) == 1:
        return "pass"
    else:
        return "fail"

def paths(subway):
    nlines = len(subway[0])

    ## There are really [1, len(subway)-1] steps.  See comment at top of file.
    for i in range(8):
        for path in product(range(nlines), repeat=i+1):
            yield path

def possibleOrders(subway):
    orders = []
    for path in paths(subway):
        orders.append(path)
    return orders

def removeStation(subway, station):
    station_routes = subway[station]
    s = deepcopy(subway)
    s = s[:station] + s[station+1:]
    for i in range(0, len(s)):
        for j in range(0, len(s[i])):
            if s[i][j] > station:
                s[i][j] -= 1
            elif s[i][j] == station:
                if station_routes[j] == station:
                    s[i][j] = i
                else:
                    s[i][j] = station_routes[j]
    return s

def take_path(subway, station, path):
    for line in path:
        station = subway[station][line]
    return station

def test_path(subway, path):
    end_station = -1
    for station in range(len(subway)):
        s = take_path(subway, station, path)
        if end_station < 0:
            end_station = s
        if end_station != s:
            return False
    return True


def answer69(subway):
    # initial test
    orders = possibleOrders(subway)
    for order in orders:
        if traversePath(subway, order) == "pass":
            return -1
    # start removing one at a time
    for k in range(len(subway)):
        new_subway = removeStation(subway, k)
        for order in orders:
            if traversePath(new_subway, order) == "pass":
                return k
    return -2

def answer(subway):
    nlines = len(subway[0])
    for path in paths(subway):
        if test_path(subway, path):
            return -1
    for closed_station in range(len(subway)):
        s = remove(subway, closed_station)
        for path in paths(s):
            if test_path(s, path):
                return closed_station
    return -2

subway = [[0, 1, 2, 3, 4, 5], [2, 0, 4, 1, 3, 4], [1, 1, 5, 1, 3, 4], [3, 5, 4, 1, 1, 2], [0, 4, 1, 3, 0, 5], [5, 5, 5, 5, 5, 1]]
#subway = [[0, 0, 0, 1, 2], [1, 1, 1, 2, 2], [2, 1, 2, 0, 0]]
#subway = [[0, 1, 2], [0, 1, 2], [2, 0, 1]]
#subway = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
#subway = [[4, 4, 4, 4, 4], [4, 4, 4, 4, 4], [], [], [], [], [], [], [], [], [], [], []]

#print test_path(removeStation(subway, 0), possibleOrders(subway)[0])
print test_path(subway, [0, 1, 0, 0, 0, 0])








