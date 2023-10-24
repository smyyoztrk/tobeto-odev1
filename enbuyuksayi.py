sayi1=float(input(""))
sayi2=float(input(""))
sayi3=float(input(""))

if sayi1>sayi2:
    if sayi1>sayi3:
        print(f"en büyük sayı:{sayi1}")
elif sayi2>sayi3:
    if sayi2>sayi1:
        print(f"en büyük sayı:{sayi2}")
elif sayi3>sayi1:
    if sayi3>sayi2:
        print(f"en büyük sayı:{sayi3}")
else:
    print("sayılar eşit")


