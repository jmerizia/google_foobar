# Carrot Land (TRIAL)

# The goal here will be to find the two points
# that are on the far left and far right. Then,
# the triangle will be determined to be pointed
# down or pointed up. The script will then have
# three line equations and a grid of
# coordinates to parse through/test. To do this
# efficiently, the script will come in from the
# top on each possible column and test each row
# of the column until a viable point is found.
# This process will be repeated form the bottom
# and the number of points in total will then
# be calculated.

def answer(vertices):

    A = vertices[0] # far left point
    B = vertices[2] # far right point
    C = vertices[0] # top/bottom point

    # sort the points A & B:
    for vertex in vertices:
        if vertex[0] < A[0]:
            A = vertex
        elif vertex[0] > B[0]:
            B = vertex
    # sort point C:
    for vertex in vertices:
        if vertex != A and vertex != B:
            C = vertex

    # slope of main line:
    m = (float(B[1]) - float(A[1])) / (float(B[0]) - float(A[0]))

    # find y value:
    y = m * (float(C[0]) - float(A[0])) + float(A[1])

    # compare y values,
    # determine direction and max/min values:
    if C[1] > y:
        direction = "up"
        max_y = sorted([C[1], A[1], B[1]])[2] - 1
        min_y = sorted([A[1], B[1]])[0] + 1
    else:
        direction = "down"
        min_y = sorted([C[1], A[1], B[1]])[0] + 1
        max_y = sorted([A[1], B[1]])[1] - 1

    min_x = A[0] + 1
    max_x = B[0] - 1

    # slopes of lines one and two:
    m1 = (float(C[1]) - float(A[1])) / (float(C[0]) - float(A[0]))
    m2 = (float(C[1]) - float(B[1])) / (float(C[0]) - float(B[0]))

    across_main = {}
    across_two = {}

    # perform the search:
    cursor_x = min_x
    while cursor_x <= max_x:

        y = m * (float(cursor_x) - float(A[0])) + float(A[1])
        y1 = m1 * (float(cursor_x) - float(C[0])) + float(C[1])
        y2 = m2 * (float(cursor_x) - float(C[0])) + float(C[1])

        if direction is "down":

            cursor_y = max_y
            while cursor_y >= min_y:
                if cursor_y < y:
                    across_main[cursor_x] = cursor_y
                    # don't continue
                    cursor_y = min_y - 1
                cursor_y -= 1

            cursor_y = min_y
            while cursor_y < max_y:
                if cursor_y > y1 and cursor_y > y2:
                    across_two[cursor_x] = cursor_y
                    # don't continue
                    cursor_y = max_y + 1
                cursor_y += 1

        elif direction is "up":

            cursor_y = min_y
            while cursor_y <= max_y:
                if cursor_y > y:
                    across_main[cursor_x] = cursor_y
                    # don't continue
                    cursor_y = max_y + 1
                cursor_y += 1

            cursor_y = max_y
            while cursor_y >= min_y:
                if cursor_y < y1 and cursor_y < y2:
                    across_two[cursor_x] = cursor_y
                    # don't continue
                    cursor_y = min_y - 1
                cursor_y -= 1

        cursor_x += 1

    #return across_two, across_main

    # now count the number of integer coordinates
    total = 0

    cursor_x = min_y
    while cursor_x <= max_x:
        if cursor_x in across_main:
            total += abs(across_main[cursor_x] - across_two[cursor_x]) + 1
        cursor_x += 1

    return total


print answer([[91207, 89566], [-88690, -83026], [67100, 47194]])






