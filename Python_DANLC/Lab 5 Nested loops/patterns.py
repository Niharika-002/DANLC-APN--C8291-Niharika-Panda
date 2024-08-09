# Create Following Patterns using functions in a single program:-

def first_pattern(b):
    for i in range(1, b + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()


first_pattern(5)


def second_pattern(c):
    for i in range(1, c + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


second_pattern(5)


def third_pattern(d):
    number = 1
    for i in range(1, d + 1):
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1
        print()


third_pattern(5)


def fourth_pattern(e):
    for i in range(1, e + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


fourth_pattern(5)


def fifth_pattern(f):
    for i in range(f):
        for j in range(1, f - i):
            print(" ", end=" ")
        for k in range(1, i + 2):
            print(k, end=" ")
        print()


fifth_pattern(5)


def sixth_pattern(g):
    for i in range(1, g + 1):
        for j in range(g - i, 0, -1):
            print(j, end=" ")
        print()


sixth_pattern(6)


def seventh_pattern(h):
    for i in range(h, 0, -1):
        print(" " * (h - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        print()


seventh_pattern(5)


def number_diamond(l):
    for i in range(1, l + 1):
        # Print leading spaces
        for j in range(l - i):
            print(" ", end="")
        # Print numbers in ascending order
        for k in range(1, i + 1):
            print(k, end="")
        # Print numbers in descending order
        for y in range(i - 1, 0, -1):
            print(l, end="")
        print()

    # Lower part of the diamond
    for i in range(l - 1, 0, -1):
        # Print leading spaces
        for j in range(l - i):
            print(" ", end="")
        # Print numbers in ascending order
        for k in range(1, i + 1):
            print(k, end="")
        # Print numbers in descending order
        for y in range(i - 1, 0, -1):
            print(l, end="")
        print()


number_diamond(6)


def InvertedHalfPyramid(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 2):
            print(j, end=" ")
        print(" ")


InvertedHalfPyramid(5)


def hollowHalfPyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # if i = j and i = n and j = 1:
            print(" ", end=" ")
            # else:
            print(j, end=" ")
        print(" ")


hollowHalfPyramid(5)


def fullHollowPyramid(n):
    for i in range(1, n + 1):
        for j in range(n - 1, i - 1, -1):
            print(" ", end=" ")

    for j in range(i, 2 * i):
        print(j, end=" ")

    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")
    print()


fullHollowPyramid(6)


def fullPyramid(n):
    for i in range(1, n + 1):
        for j in range(n - 1, i - 1, -1):
            print(" ", end=" ")

        for j in range(i, 2 * i):
            print(j, end=" ")

        for j in range(2 * i - 2, i - 1, -1):
            print(j, end=" ")
        print()


fullPyramid(6)


def fullHollowPyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")

    for j in range(1, 2 * i):
        if i == n or j == 1 or j == 2 * i - 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()


def invertedHalfPyramid(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 2):
            if j == 1 or i == 1 or i + j == 6:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print(" ")


invertedHalfPyramid(6)

# Alphabet PYRAMID
for r in range(65, 91):
    for s in range(90, r, -1):
        print(end="  ")
    for c in range(65, r + 1):
        print(chr(c), end=" ")
    for c1 in range(c - 1, 64, -1):
        print(chr(c1), end=" ")

    print()


