#2
integer=10
if integer>10:
    print("Greater than 10")
elif integer==10:
    print("Equal to 10.")
else:
    print("Less than 10.")
print("")

#3
print("")
asked_num=input("Insert num: ")
if int(asked_num)==15:
    print("Equal to 15.")
else:
    print("Not equal to 15.")
print("")

#4
asked_group=input("Insert group num: ")
if int(asked_group)==92:
    print("Correct.")
else:
    print("Wrong")
print("")

#5
for i in range(50,101,5):
    print(i)
print("")

#6
for i in range(6):
    print("My name is A and I'm Infinity years old.")
print("")

#7
while_num=20
while int(while_num)<51:
    print(while_num)
    while_num=while_num+1
print("")

#8
print("For loop:")
for i in range(100):
    print(i)
print("")
print("While loop:")
while_num=0
while int(while_num)<100:
    print(while_num)
    while_num=while_num+1
print("")

#9
print("For loop:")
for i in range(101):
    print(i)
print("")
print("While loop:")
while_num=0
while int(while_num)<101:
    print(while_num)
    while_num=while_num+1
print("")

#10
print("For loop:")
for i in range(10,20):
    print(i)
print("")
print("While loop:")
while_num=10
while int(while_num)<20:
    print(while_num)
    while_num=while_num+1
print("")

#11
print("For loop:")
for i in range(100,201,5):
    print(i)
print("")
print("While loop:")
while_num=100
while int(while_num)<201:
    print(while_num)
    while_num=while_num+5
print("")

#12
for i in range(-10,1):
    print(i*-1)
print("")

#13
choose_num=input("Insert number: ")
if float(choose_num)<=-1:
    print("Negative number.")
elif float(choose_num)>=1:
    print("Plus Number.")
elif float(choose_num)==0:
    print("Zero.")
else:
    print("N/A")
print("")

#14
age=input("Insert age: ")
if int(age)==0 or int(age)<12:
    print("ბავშვი ხარ.")
elif int(age)==13 or int(age)<19:
    print("მოზარდი/თინეიჯერი ხარ.")
elif int(age)==20 or int(age)<64:
    print("ზრდასრული ხართ.")
elif int(age)==65 or int(age)<120:
    print("ხანში შესული ხართ.")
elif int(age)>=120:
    print("გურუ ან ჯადოქარი.")
else:
    print("არასწორი ინფო.")
print("")

#15
num1=input("First num: ")
num2=input("Second num: ")
num3=input("Third num: ")
if float(num1)>float(num2) and float(num1)>float(num3):
    print(num1)
elif float(num2)>float(num1) and float(num2)>float(num3):
    print(num2)
elif float(num3)>float(num1) and float(num3)>float(num2):
    print(num2)
else:
    print("ERROR")
print("")

#16
month=input("Insert day num 1-7: ")
if int(month)==1:
    print("ორშაბათი")
elif int(month)==2:
    print("სამშაბათი")
elif int(month)==3:
    print("ოთხშაბათი")
elif int(month)==4:
    print("ხუთშაბათი")
elif int(month)==5:
    print("პარასკევი")
elif int(month)==6:
    print("შაბათი")
elif int(month)==7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")
print("")

#17
num=input("Insert num: ")
if int(num)>=50:
    print(int(num)*5)
else:
    print(int(num)*int(num))
print("")

#18
password=input("Insert password: ")
if password=="goa123":
    print("Correct!")
else:
    print("Wrong")
print("")

#19
num=input("Insert num: ")
for i in range(1,int(num)+1):
    print(int(num)+i)
print("")

#20
for i in range(1,5001):
    if i==2024:
        print("JACKPOT!")
        break
print("")

#21
for i in range(1,300):
    if i%4==0:
        if i%7==0:
            print(i)
        else:
            continue
    else:
        continue
print("")

#22
for i in range(10,51):
    if i%10==0:
        continue
    else:
        print(i)
print("")