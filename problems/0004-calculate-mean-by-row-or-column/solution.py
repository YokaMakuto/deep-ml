
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    n = len(matrix[0]) 
    m = len(matrix)     

    c: list[float] = [0.0] * n
    b: list[float] = [0.0] * m

    if mode == "column":
        for i in range(n):
            for j in range(m):
                c[i] += matrix[j][i] / m
        return c

    else:
        for i in range(m):
            for j in range(n):
                b[i] += matrix[i][j] / n
        return b
