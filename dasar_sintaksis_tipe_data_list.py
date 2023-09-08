daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
print('tampilkan variable daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')

for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\n tampilkan dengan for in range')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'kenji volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\n Kembalikan nilai awal daftar_buku')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
print('\nTambahkan 1 buku baru' )
daftar_buku.append('Dunia matematika kelas 5')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\n Clear list')
daftar_buku.clear()
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
daftar_buku[0] = 'eight habits'
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
daftar_buku.pop(-4)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])
