def mat_add(m1, m2):
    m = len(m1)
    n = len(m1[0])
    if m != len(m2) or n != len(m2[0]):
        print("Cant perform addition")
        return 0
    m3 = [[m1[i][j] + m2[i][j] for j in range(n)] for i in range(m)]
    return m3


def mat_sub(m1, m2):
    m = len(m1)
    n = len(m1[0])
    if m != len(m2) or n != len(m2[0]):
        print("Cant perform subtraction")
        return 0
    m3 = [[m1[i][j] - m2[i][j] for j in range(n)] for i in range(m)]
    return m3


def mat_mul(m1, m2):
    m = len(m1)
    n = len(m1[0])
    p = len(m2)
    q = len(m2[0])
    if n != p:
        print("Cant perform multiplication")
        return 0
    m3 = [[0 for i in range(q)] for j in range(m)]
    for k1, v1 in enumerate(m1):
        for k2, v2 in enumerate(m2[0]):
            s = 0
            for k3, v3 in enumerate(m1[0]):
                s += m1[k1][k3] * m2[k3][k2]
            m3[k1][k2] = s
    return m3


def transpose(m1):
    m = len(m1)
    n = len(m1[0])

    m2 = [[m1[j][i] for j in range(m)] for i in range(n)]
    return m2


m_len1, n_len1 = map(int, input("Enter the dimensions of matrix1: ").split())
m_len2, n_len2 = map(int, input("Enter the dimensions of matrix2: ").split())
mat1 = [[int(input("Enter elements of matrix1: ")) for j1 in range(n_len1)] for i1 in range(m_len1)]
mat2 = [[int(input("Enter elements of matrix2: ")) for j2 in range(n_len2)] for i2 in range(m_len2)]

mat_add(mat1, mat2) and print("Addition: ", mat_add(mat1, mat2))
mat_sub(mat1, mat2) and print("Subtraction: ", mat_sub(mat1, mat2))
mat_mul(mat1, mat2) and print("Multiplication: ", mat_mul(mat1, mat2))
print("Transposition of matrix 1: ", transpose(mat1), "\nTransposition of matrix 2: ", transpose(mat2))
