i = input('Sudah makan..? [y/n]: ')     # input adalah untuk memasukkan jawaban

if i == 'y':
    print('Saya sudah makan')
elif i == 'n':                          # elif adalah else if
    print('Saya belum makan')
else:
    print('Maaf Input salah')