

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length")
    return sum(x * y for x, y in zip(a, b))


def matrix_multiply(A, B):

    if not A or not B:
        raise ValueError("Input matrices cannot be empty")
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")

    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def conditional_probability(events):

    a_and_b = events.get('A_and_B')
    b = events.get('B')
    if b == 0:
        raise ZeroDivisionError("P(B) cannot be zero")
    return a_and_b / b


# Optional: Test the functions when run directly
if __name__ == "__main__":
    print("Dot Product:", dot_product([1, 2, 3], [4, 5, 6]))  # 32
    print("Matrix Multiply:", matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # [[19, 22], [43, 50]]
    print("Conditional Probability:", conditional_probability({'A_and_B': 120, 'B': 400}))  # 0.3
