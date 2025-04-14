# 📘 Perkalian Matriks 5x5 di Python (Tanpa NumPy)

Program ini melakukan **perkalian dua matriks 5x5** tanpa menggunakan library seperti NumPy. Matriks dikalikan menggunakan perulangan `for` dan disimpan menggunakan `append`.

---

## 🧮 Matriks Input

### Matriks A:

```
| 31   5   20   6   2  |
|  3   5    1   7  10  |
|  2   3   13  14  15  |
|  6  17    2  12  20  |
|  4   5    1  23   3  |
```

### Matriks B:

```
| 1   0   0   0   1 |
| 0   1   0   1   0 |
| 0   0   1   0   0 |
| 0   1   0   1   0 |
| 1   0   0   0   1 |
```

---

## 🔧 Cara Kerja Kode

### Inisialisasi Matrix

```python
hasil = []
```

### Penjelasan:

- Melakukan Inisalisasi untuk hasil dari matrix

---

```python
hasil = []  # Matriks hasil kosong

for i in range(5):         # Untuk setiap baris di A
    baris = []
    for j in range(5):     # Untuk setiap kolom di B
        total = 0
        for k in range(5): # Perkalian elemen baris A dengan kolom B
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)
```

### Penjelasan:

- Kita mengambil **baris ke-i dari A** dan **kolom ke-j dari B**.
- Mengalikan elemen yang bersesuaian lalu menjumlahkannya.
- Hasilnya adalah elemen `[i][j]` pada matriks `hasil`.

---

## ✅ Contoh Perhitungan Elemen `hasil[0][0]`

Baris pertama A: `[31, 5, 20, 6, 2]`  
Kolom pertama B: `[1, 0, 0, 0, 1]`

```
= 31×1 + 5×0 + 20×0 + 6×0 + 2×1
= 31 + 0 + 0 + 0 + 2
= 33
```

---

## 📊 Matriks Hasil

Hasil dari `A x B` adalah:

```
[33, 11, 20, 11, 33]
[13, 12, 1, 12, 13]
[17, 17, 13, 17, 17]
[26, 49, 2, 49, 26]
[7, 28, 1, 28, 7]
```

---

## 🔍 Ringkasan

- Tidak menggunakan library eksternal seperti `numpy`.
- Operasi dilakukan sepenuhnya dengan nested loops dan list native Python.
- Cocok untuk pembelajaran dasar matriks dan algoritma perkalian manual.
