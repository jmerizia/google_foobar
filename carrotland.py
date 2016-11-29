# Carrot Land

# The way I solved this puzzle was by first determining
# the number of lattice points that are located on the
# boundary line of the triangle. This value is based on
# the gcds of the numerator and denominator of the
# slopes of each line segment. Then, I found the area
# of the triangle using a variation of Gauss's shoelace
# formula. Finally, I used Pick's theorem to find the
# number of internal lattice points. The coolest part
# about this solution is that it CAN be written
# entirely on one line. I included the one line
# solution below. It's not very readable, but it works!

from fractions import gcd

def answer(vertices):
    A = vertices[0]
    B = vertices[1]
    C = vertices[2]

    # find boundary lattice points:
    pointsAB = gcd(abs(B[0] - A[0]), abs(B[1] - A[1]))
    pointsBC = gcd(abs(B[0] - C[0]), abs(B[1] - C[1]))
    pointsAC = gcd(abs(A[0] - C[0]), abs(A[1] - C[1]))

    b = pointsAB + pointsBC + pointsAC

    # find the area
    part1 = float(A[0]) * (float(B[1]) - float(C[1]))
    part2 = float(B[0]) * (float(C[1]) - float(A[1]))
    part3 = float(C[0]) * (float(A[1]) - float(B[1]))

    area = abs(part1 + part2 + part3) / 2

    # find internal lattice points
    i = area - (b / 2) + 1

    return int(i)

## Solution on one line: 
#
#def answer(vertices):
#    return int((abs(float(vertices[0][0]) * (float(vertices[1][1]) - float(vertices[2][1])) + float(vertices[1][0]) * (float(vertices[2][1]) - float(vertices[0][1])) + float(vertices[2][0]) * (float(vertices[0][1]) - float(vertices[1][1]))) / 2) - ((gcd(abs(vertices[1][0] - vertices[0][0]), abs(vertices[1][1] - vertices[0][1])) + gcd(abs(vertices[1][0] - vertices[2][0]), abs(vertices[1][1] - vertices[2][1])) + gcd(abs(vertices[0][0] - vertices[2][0]), abs(vertices[0][1] - vertices[2][1]))) / 2) + 1)