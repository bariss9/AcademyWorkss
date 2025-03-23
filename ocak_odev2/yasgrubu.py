#yaşa göre gruplandırma programı

age = int(input("Lütfen yaşınızı giriniz: "))

if age < 0 :
    print("Lütfen geçerli bir yaş giriniz.")
elif age < 13:
    print(f"{age} yaş: Çocuk grubu.")
elif age < 20:
    print(f"{age} yaş: Genç grubu.")
elif age < 60:
    print(f"{age} yaş: Yetişkin grubu.")
elif age >= 60:
    print(f"{age} yaş: Yaşlı grubu.")

