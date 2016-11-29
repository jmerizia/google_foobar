# Carrot Land (in one line)

def answerr(vertices):
    return int((abs(float(vertices[0][0]) * (float(vertices[1][1]) - float(vertices[2][1])) + float(vertices[1][0]) * (float(vertices[2][1]) - float(vertices[0][1])) + float(vertices[2][0]) * (float(vertices[0][1]) - float(vertices[1][1]))) / 2) - ((gcd(abs(vertices[1][0] - vertices[0][0]), abs(vertices[1][1] - vertices[0][1])) + gcd(abs(vertices[1][0] - vertices[2][0]), abs(vertices[1][1] - vertices[2][1])) + gcd(abs(vertices[0][0] - vertices[2][0]), abs(vertices[0][1] - vertices[2][1]))) / 2) + 1)