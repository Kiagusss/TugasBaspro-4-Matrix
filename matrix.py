A = [
    [31, 5, 20, 6, 2],
    [3, 5, 1, 7, 10],
    [2, 3, 13, 14, 15],
    [6, 17, 2, 12, 20],
    [4, 5, 1, 23, 3]
]

B = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

# Inisialisasi matriks hasil sebagai matriks kosong
hasil = []

# Perkalian matriks
for i in range(5):
    baris = []  # baris untuk hasil[i]
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)

# Menampilkan hasil
print("Hasil perkalian matriks A x B:")
for row in hasil:
    print(row)
