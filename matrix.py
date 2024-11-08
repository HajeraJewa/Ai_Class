import numpy as np

# Matriks A (3x2)
A = [[2, 0],
    [-3, 1],
    [4, 5]]

# Matriks B (2x2)
B = [[3, 1],
    [-1, 0]]

# Matriks C (2x2)
C = [[4, 7],
    [2, 1]]

# -- Menggunakan library (numpy) --
A_np = np.array(A)
B_np = np.array(B)
C_np = np.array(C)

# Menghitung AB dan AC dengan numpy
AB_np = np.dot(A_np, B_np)
AC_np = np.dot(A_np, C_np)

# Menjumlahkan (AB + AC) dengan numpy
result_np = AB_np + AC_np

# Tampilkan hasil menggunakan numpy
print("Hasil menggunakan numpy:")
print("Matriks AB:\n", AB_np)
print("Matriks AC:\n", AC_np)
print("Hasil (AB + AC):\n", result_np)

# --- Tanpa library (Manual) ---

# Fungsi untuk perkalian matriks secara manual
def multiply_matrices(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Fungsi untuk penjumlahan matriks secara manual
def add_matrices(X, Y):
    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    return result

# Menghitung AB dan AC secara manual
AB_manual = multiply_matrices(A, B)
AC_manual = multiply_matrices(A, C)

# Menjumlahkan (AB + AC) secara manual
result_manual = add_matrices(AB_manual, AC_manual)

# Tampilkan hasil menggunakan metode manual
print("\nHasil menggunakan metode manual:")
print("Matriks AB:\n", AB_manual)
print("Matriks AC:\n", AC_manual)
print("Hasil (AB + AC):\n", result_manual)