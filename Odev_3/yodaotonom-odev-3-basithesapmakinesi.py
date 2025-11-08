sonuc = 0
while True:
    sayi1 = int(input("İlk Sayınızı Girin: "))
    sayi2 = int(input("İkinci Sayınızı Girin: "))

    islem = input("Yapmak İstediğiniz İşlemi Seçin (+ , - , * , /):  ")

    if islem == "+":
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    elif islem == "*":
        sonuc = sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            print("Bir Sayı Sıfıra Bölünmez!!!")
        else:
            sonuc = sayi1 / sayi2

    print("Sonuc: ", sonuc)

    istek = input("Çıkmak İstiyorsanız (e) Devam Etmek İstiyorsanız (h) Yazınız.")

    if istek == "e":
        print("İyi Günler Reis.")
        break
    else:
        continue

