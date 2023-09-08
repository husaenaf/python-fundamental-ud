"""
perulangan dengan while untul studi kasus baca buku
"""

book_count = 10
print('ibu berkata, "baca semua bukumu"')
read_count = 0

understood_count = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"buku ke {understood_count + 1} belum paham")
    else:
        understood_count +=1
        #arti kode diatas adalah jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
        print(f"buku ke {understood_count} sudah dibaca dan dipahami")

print(f'jumlah buku yang sudah dibaca dan dipahami {understood_count}')
if understood_count == book_count:
    print(f'bu, semua buku sudah dibaca dan dipahami')
else:
    print(f"bu, tidak semua buku bisa dipahami. "
          f"Budi hanya bisa memahami {understood_count} buku")
