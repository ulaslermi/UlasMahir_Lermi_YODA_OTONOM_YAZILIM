metin = input("Küçük Harflerden Oluşan Bir Metin Giriniz: ")

metinCevirme = metin.lower()
k elimeler= metinCevirme.split()

enUzunKelime = max(metin.split(), key=len)
toplamKelimeSayisi = len(metin.split())
toplamKarakterSayisi = len(metin)
enUzunKelimeninUzunlugu = len(enUzunKelime)

tekrarEtmeSayisi = {}

print(f"Metininde Toplam Kelime Sayısı {toplamKelimeSayisi}.")
print(f"Toplam Karakter Sayısı {toplamKarakterSayisi}.")
print(f"En Uzun Kelimenin Uzunluğu {enUzunKelimeninUzunlugu}.")

for kelime in kelimeler:
    if kelime in tekrarEtmeSayisi:
        tekrarEtmeSayisi[kelime] += 1
    else:
        tekrarEtmeSayisi[kelime] = 1

for kelime , adet in tekrarEtmeSayisi.items():
    print(f"{kelime} kelimesi {adet} defa metinde geçti.")







