import random

bilincek_sayi =random.randint(1,100)

print("Merhabalar Sayı Tahmin Etme Oyununa Hoşgeldiniz.")
print("1 ile 100 Arasında Bir Sayı Tahmin Ediceksiniz.")
print("10 Hakkınız Vardır.")

tahmin_sayisi = 1

while True:

    tahmin = int(input(f"{tahmin_sayisi}. tahmin hakkınızdaki tahmininiz: "))
    tahmin_sayisi += 1
    if tahmin_sayisi == 10:
        print("Bütün Haklarınız Bitmiştir")
        break

    if tahmin > bilincek_sayi:
        print("Daha Küçük Bir Sayı Seçiniz.")
    elif tahmin < bilincek_sayi:
        print("Daha Büyük Bir Sayı Seçiniz.")
    else:
        print(f"Tebrikler Doğru Sayı {bilincek_sayi}.Doğru Sayıyı {tahmin_sayisi} denemede buldun.")
        break




