"""
perulangan dengan while untul studi kasus baca buku
"""

jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca +=1
    #arti kode diatas adalah jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print('\n contoh lainnya adalah')
i = 0                            # Nilai awal Untuk Membatasi Loop
while i < 5:                     # ketika i lebih kecil dari 5 maka eksekusi kode selanjutnya dan diulang
    i +=1                        # i = i + 1
    print(f'perulangan ke {i}')