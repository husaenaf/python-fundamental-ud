#sekuensial

print('Ibu berkata, "pergi ke toko"')
print('Budi menjawab, "baik, apa yang harus saya lakukan di toko?"')
print('ibu menjawab,"Beli satu botol susu"')
print('maka budi berangkat ke toko')
print('dan mulai berbelanja')


#percabangan
jumlah_botol_susu = 173
jumlah_telur = 150

#pola penulisan python lama, dibawah ini
#print("Jumlah botol susu", jumlah_botol_susu, "btl")
#pola penulisan python yang baru, dibawah ini
print(f"jumlah botol susu {jumlah_botol_susu} btl")
print(f"jumlah telur {jumlah_telur} btl")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya dan ternyata uangnya cukup")
if jumlah_telur > 5:
    print("Budi membeli 1 botol susu")
    print("Budi membeli 6 telur")
else:
    print("Budi membeli 1 botol susu")
    print("budi pulang ke rumah")
    print("menyampaikan hasilnya kepada ibunya")