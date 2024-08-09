# Write a function `transpose(matrix)` that takes a matrix (list of lists) and returns its transpose.

def create_transpose(mtrx):
    if not mtrx:
        return[]
    rows = len(mtrx)
    cols = len(mtrx[0])

    transposed = [[None] * rows for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            transposed[c][r] = mtrx[r][c]

    return transposed


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = create_transpose(matrix)
print(transposed_matrix)