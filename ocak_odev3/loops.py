
# 1'den 100'e kadar olan sayıları ekrana yazdıran program

for i in range (100):
    print(f"{i}") 

# 1'den 100'e kadar olan çift sayılar
print("Çift sayılar")
for k in range (0, 100, 2):
    print(f"{k}")

print("**********************")
print("**********************")
#faktöriyel hesabı

num1 = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))
result = 1
for i in range(2, num1+1):
    result = result * i
print(result) 

print("**********************")
print("**********************")
#1'den 100'e kadar asal sayıları yazdıran program

for num in range(2, 101):  
    prime = True 
    for i in range(2, int(num ** 0.5) + 1):  # herhangi bir sayının asal olup olmama kontrolü
        if num % i == 0:
            prime = False
            break  
    if prime:
        print(num)  

