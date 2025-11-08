class BankaHesabi:

    def __init__(self,ad, hesapNumara, bakiye = 0):
        self.ad = ad
        self.hesapNumara = hesapNumara
        self.bakiye = bakiye


    def paraYatirma(self , miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"Para yatırma işlemi gerçekleşti Güncel Bakiye {self.bakiye} TL.")
        else:
            print("Yanlış Miktar Girdiniz.")

    def paraCekme(self  ,miktar):
        if miktar > self.bakiye:
            print("Bakiye yetersiz")
        elif miktar <= 0:
                print("Geçersiz bir miktar.")
        else:
                self.bakiye -= miktar
                print(f"Kalan Bakiye {self.bakiye} TL.")

    def bakiyeGoruntuleme(self):
        print(f"Hesap Sahibi: {self.ad} .")
        print(f"Hesap Numara: {self.hesapNumara} .")
        print(f"Güncel Bakiye {self.bakiye} TL.")


hesapSahibi = input("Hesap sahibinin adını girin: ")
hesapNo = input("Hesap numarasını girin: ")

benimHesabim = BankaHesabi(hesapSahibi, hesapNo, 0)

while True:
    print("1: Bakiye Görüntüle")
    print("2: Para Yatır")
    print("3: Para Çek")
    print("q: Çıkış")
    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/q): ")

    if secim == 'q':
        print("İyi Günler Reis.")
        break

    elif secim == '1':
        benimHesabim.bakiyeGoruntuleme()
    if secim == '2':
        miktar = float(input("Yatırmak İstediğiniz Miktarı Girin:"))
        benimHesabim.paraYatirma(miktar)
    elif secim == '3':
        miktar = float(input("Çekmek İstediğiniz Miktarı Girin:"))
        benimHesabim.paraCekme(miktar)

