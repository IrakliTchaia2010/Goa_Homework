#1
age=int(input("Input age: "))
if age>=18:
    print("თქვენ სრულწლოვანი ხართ, წვდომა ნებადართულია!")
else:
    print("წვდომა უარყოფილია! თქვენ ჯერ კიდევ არასრულწლოვანი ხართ.")
print("")

#2
#while ციკლის გამოყენებით მომხმარებელს იმდენჯერ სთხოვე ტექსტის შემოყვანა სანამ მისი ტექსტი არ დაემთხვევა სიტყვა "unique"-ს.
word="unique"
sentence=input(str("Insert sentence: "))
while word!=sentence:
    if word==sentence:
        print("You guessed it correctly!")
    else:
        print("Try again.")
        sentence=input(str("Insert sentence: "))
print("")

#3
num=10
if num%2:
    print("რიცხვი"+" "+str(num)+" "+"არის ლუწი.")
else:
    print("რიცხვი"+" "+str(num)+" "+"არის კენტი.")
print("")

#4
num1=0
num2=100
for i in range(int(num1),int(num2),3):
    print("HELLO, WORLD!")
print("")

# #5
# for i in range(1,31,5):
#     if i%2==0:
#         print(i)