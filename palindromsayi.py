
try:
    sayistring=input("")
    sayi=int(sayistring)
    basamak=len(sayistring)
    sayac=basamak//2
    sayac2=basamak-1

    if 0<=sayi<=9:
        print(f"{sayi} palindrom sayıdır")
    elif sayi>9:
        for i in range(sayac):
            if sayistring[i]==sayistring[sayac2]:
                sayac2-=1
                if i==sayac-1:
                    print(f"{sayi} palindrom sayıdır")
            else:
                print(f"{sayi} palindrom sayı değildir")
                break
except:
    print("yanlış deger girdiniz,doğal sayı giriniz")
