"""
perulangan dengan while untul studi kasus baca buku
"""

jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0

while jumlah_buku_yang_sudah_dibaca < 10:
    jumlah_buku_yang_sudah_dibaca +=1
    print(f"buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')