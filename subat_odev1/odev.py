#Calculator

def sum(num1, num2):
    return num1 + num2

def div(num1, num2):
    return num1/num2

def product(num1, num2):
    return num1*num2

def extraction(num1, num2):
    return num1-num2

def calculator(num1, num2):
    print(f"Sum = {sum(num1, num2)}")
    print(f"Division = {div(num1, num2)}")
    print(f"Product = {product(num1, num2)}")
    print(f"Extraction = {extraction(num1, num2)}")
    

calculator(4, 8)

# Kaç yıl sonra 100 yaşında olacağım?

age = int(input("Please enter your age: "))
if age<100:
    print(f"You will 100 years old after {100-age}")
elif age>100:
    print("You are pass your 100's age")
else:
    print("You are 100 years old")    
    
    
#palindrom
def palindrom(word):
    word = word.lower() 
    return word == word[::-1]  # Pythonda kelimeyi tersine çevirmenin en kolay yöntemi

word = input("Enter your word: ")
if palindrom(word):
    print(f"'{word}' is palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
