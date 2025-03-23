#kullanıcının girdiği sayıya göre ders notunun harf karşılığını veren program
grade = int(input("Lütfen notunuzu giriniz: "))

if grade < 0 or grade > 100:
    print("Lütfen geçerli bir not giriniz.")
elif grade < 60:
    print(f"{grade} harf olarak F düşer.")
elif grade < 70:
    print(f"{grade} harf olarak D düşer.")
elif grade < 80:
    print(f"{grade} harf olarak C düşer.")
elif grade < 90:
    print(f"{grade} harf olarak B düşer.")
elif grade <= 100:
    print(f"{grade} harf olarak A düşer.")
