masalar = dict()

for a in range(20):
    masalar[a] = 0 #bakiye

def hesap_ekle():
    masa_no = int(input("Masa numarası:  "))
    bakiye = masalar[masa_no]
    eklenecek_ucret = float(input("Eklenecek ücret: "))
    guncel_bakiye = bakiye + eklenecek_ucret
    masalar[masa_no]=guncel_bakiye
    print("İşleminiz tamamlandı!")

def hesap_odeme():
    masa_no= int(input("Masa numarası: "))
    bakiye = masalar[masa_no]
    odenecek_hesap= float(input("Ödenecek ücret: "))
    guncel_bakiye= bakiye - odenecek_hesap
    masalar[masa_no]=guncel_bakiye
    print("İşleminiz tamamlandı! Kalan borç: {}".format(guncel_bakiye))

def dosya_kontrolü(dosya_adi):
    try:
         #dosya varsa verileri içerisinden alacağız.
        dosya= open(dosya_adi,"r",encoding="utf-8")
        veri= dosya.read()
        veri = veri.split("\n")
        veri.pop() # boş elemanları siler.
        dosya.close()
        for a in enumerate(veri): #index numaralarını eşitler.
            masalar[a[0]] = float(a[1])
    except FileNotFoundError:
        dosya= open(dosya_adi,"w",encoding="utf-8")
        dosya.close()
        print("Kayıt dosya oluşturuldu!")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")


def dosya_guncelle(dosya_adi):
    dosya= open(dosya_adi,"w",encoding="utf-8")
    for a in range(20):
        bakiye=masalar[a]
        bakiye= str(bakiye) # dosyamız string veriler tutabiliyor.
        dosya.write(bakiye+"\n")
    dosya.close()


def ana_islemler():
    dosya_kontrolü("bakiye.txt")
    while True:
        print("""
            Şevin Sönmez Restaurant Uygulaması
            
        1) Masaları Görüntüle
        2) Hesap Ekle
        3) Hesap Ödeme
        q) Çıkış
        """
        )

        secim = input("Yapılacak işlemi giriniz: ")
        if secim =="1":
            for a in range(20):
                print("Masa {} için hesap : {} ".format(a,masalar[a]))

        elif secim=="2":
            hesap_ekle()

        elif secim=="3":
            hesap_odeme()
        elif "Q" or "q":
            print("Çıkış yapılıyor. İyi Günler!")
            quit()
        else:
            print("Lütfen geçerli bir işlem giriniz! ")
        dosya_guncelle("bakiye.txt")
        input("Ana menüye devam etmek için Enter'layınız.")

ana_islemler()