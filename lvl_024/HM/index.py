#2
# custom functions არის ალტერნატიურად ცვლადის გაშვების მეთოდი
# მაგ:
# def hi(name):
#     print("Hello",name)
# hi("A")
# def არის თავისთავად custom functionი
# "hi" არის პარამეტრი, გადაეცემა ფინქციის ფრჩხილებში შექმნისას და მნიშვნელობა ენიჭება როდესაც ხდება ფუნქციის გამოძახება არგუმენტიდან
# "(name)" არის არგუმენტი, ჯდება ფუნქციაში პარამეტრის ადგილას

#3
def math(num1,num2):
    print(num1+num2)
math(1,1)
print("")

#4
def numcheck(num):
    if num%2==0:
        print("რიცხვი ლუწია")
    elif num%1==0:
        print("რიცხვი კენტია")
    else:
        print("INVALID")
numcheck(2)
print("")

#5
def quad(num):
    print(num*num)
quad(2)
print("")

#6
def upper(words):
    print(words.upper())
upper("Hello, World!")
print("")

#7
def names(first,last):
    print("First name",first,", last name",last)
names("A","a")
print("")