# Tucil1_13522078

Tugas Kecil Mata Kuliah IF 2211 Strategi Algoritma 2024 - Penyelesaian Cyberpunk 2077 Breach Protocol dengan Algoritma Brute Force

## Deskripsi Singkat Program

Program ini bertujuan untuk menemukan solusi sekuens terbaik dari minigame Breach Protocol pada game Cyberpunk 2077. Program ini menggunkan strategi brute force dalam penyelesaiannya dan ditulis dengan bahasa python. Inputan dapat berupa file .txt maupun CLI input.

## Requirements

- Python3
- library random
- library time
- pyinstaller (optional, hanya bila Anda ingin membuat .exe dari source code)

## Cara Kompilasi

Karena program ini dibuat dengan Python , maka tidak ada pengkompilasian

## Cara Menjalankan Program

Terdapat 2 metode untuk menjalankan program, yang pertama adalah dengan menggunakan .exe file, masuklah ke dalam folder bin dan jalankan .exe yang terdapat pada folder tersebut. Metode yang kedua adalah dengan cara masuk ke folder src dan mengetik berikut pada terminal :

```bash
python3 sourcecode.py
```

## Cara Menggunakan Program

Seperti yang sudah disebut di atas, terdapat dua metode dalam menginput data. Penggunaan tiap metode adalah sebagai berikut :

1. Dengan .txt file
   Buat .txt file dengan format

```
buffer_size
matrix_widthmatrix_height
matrix
number_of_sequences
sequences_1
sequences_1_reward
sequences_2
sequences_2_reward
…
sequences_n
sequences_n_reward
```

Setelah Anda buat, simpanlah .txt file tersebut pada folder input yang terdapat pada folder bin.
Perlu diperhatikan bahwa inputan ini sangat format sensitive. Penulis merekomendasikan untuk melihat beberapa contoh yang terdapat pada folder input tersebut.

2. Dengan input CLI
   Akan ada prompt yang memandu Anda dalam inputan CLI di dalam program.

## Identitas Pembuat Program

| Kelas | Nama                        | NIM      |
| ----- | --------------------------- | -------- |
| K2    | Venantius Sean Ardi Nugroho | 13522078 |
