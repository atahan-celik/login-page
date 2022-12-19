import time

hak = 3
username="admin"
password="123"

while True:
    kullanici=input("Kullanıcı Adı: ")
    sifre=input("Parola: ")
    if username==kullanici and password==sifre:
        print("Giriş başarılı!")
        break
    else:
        print("Kullanıcı adı veya parola hatalı!")
        hak-=1
        if hak>0:
            print(f"{hak} deneme hakkınız kaldı.")
        else:
            print("Deneme hakkınız doldu. 5 saniye sonra tekrar deneyin.")
            time.sleep(5)
            hak=3
