
# 5 sayı alma ve işlemler
nums = []

for i in range(5):
    num = float(input(f"{i+1}. sayıyı girin: "))
    nums.append(num)

sum = sum(nums)
avarage = sum / len(nums)
highest = max(nums)
lowest = min(nums)
print(f"sum: {sum}")
print(f"Ortalama: {avarage}")
print(f"En büyük sayı: {highest}")
print(f"En küçük sayı: {lowest}")



#kelimeyi tersten sıralama

words = []

while True:
    word = input("Bir kelime girin (Çıkmak için 'q' tuşlayın): ").strip()#striple baştaki ve sondaki gereksiz boşluklardan kurtulduk
    if word.lower() == 'q':  # flag'e bağlı çıkış kontrolü
        break
    words.append(word)

words.reverse() # pythonda tersten yazdırma fonksiyonu

print("Girilen kelimelerin ters sırası:", words)




#tekrar eden kelimeleri kaldırma
def removeDuplicates(lst):
    return list(set(lst))  # Set fonksiyonu tekrar edenleri kontrol edip kaldırmamızı sağlıyor iç içw 2 for ile de yapabilirdik

elemanlar = input("Liste elemanlarını boşlukla ayırarak girin: ").split()# burda split girilen cümledeki kelimeleri boşluklara göre listenin elemanları yapar

print("Tekrarsız liste:", removeDuplicates(elemanlar))

