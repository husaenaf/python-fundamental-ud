"""
program perulangan baca buku dengan for
"""

jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 10
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print('\nContoh sederhana lainnya')

ulang = 5                       # Variabel ini digunakan sebagai batas perulangan
for i in range(1, ulang+1):     # akan dilakukan perulangan dari 1 hingga 6 (sehingga sama dengan 5 kali perulangan)
    print(f"perulangan ke {i}") # i adalah variable loop