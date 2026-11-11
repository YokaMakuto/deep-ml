
def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    m = len(a)
    n = len(a[0])

    b: list[list[int | float]] = [[0] * m for i in range(n)]

    for i in range(m):
        for j in range(n):
            b[j][i] = a[i][j]

    return b
