def matrix_dot_vector( a: list[list[int | float]],  b: list[int | float]) -> list[int | float]:

    n = len(a)
    m = len(a[0])
    l = len(b)

    if l != m:
        return -1

    c: list[int | float] = [0] * n

    for i in range(n):
        for j in range(m):
            c[i] += a[i][j] * b[j]

    return c
