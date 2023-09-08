print('\nPerintah del')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
del daftar_buku[0:-2]  # start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
del daftar_buku[0::2]  # start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru')
daftar_buku = ['seven habits', 'How to influence people', 'first thing first', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : ganjil')
daftar_buku = ['1 seven habits', '2 How to influence people', '3 first thing first', '4 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : genap')
daftar_buku = ['1 seven habits', '2 How to influence people', '3 first thing first', '4 4DX']
daftar_buku_baru = daftar_buku[1::2]  # start stop end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : buang diujung')
daftar_buku = ['1 seven habits', '2 How to influence people', '3 first thing first', '4 4DX']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : ganjil')
daftar_buku = ['1 seven habits', '2 How to influence people', '3 first thing first', '4 4DX']
print(daftar_buku[0::2])