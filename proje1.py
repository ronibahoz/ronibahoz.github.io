print("Welcome to Simple Calculator")


sayi1 = float(input("Birinci sayiyi girin:"))

islem = input("+,-,*,/: ")

sayi2 = float(input("ikinci sayiyi girin:"))

if islem == ("+"):
    print("Sonuc:", sayi1 + sayi2)
elif islem == ("-"):
    print("Sonuc: ", sayi1-sayi2)
elif islem == ("*"):
    print("Sonuc: ", sayi1*sayi2)
elif  islem == ("/"):
    if sayi2 != 0:
        print("Sonuc: ", sayi1/sayi2)
    else:
        print("Hata sifir bölemezsin")
else:
    print("Gecersiz islem!")