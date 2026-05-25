#3
# > - მეტობა; < - ნაკლებობა; == - მკაცრი უდრისი; >= - მეტია ან ტოლია; <= - ნაკლებია ან ტოლია
print(1>5)
print(2<0)
print(4==4)
print(0.5>=0)
print(100<=1)
print("")

#4
# and - და, შეადარებს თუ რაღაცა ორივე ჭეშმარიტია თუ მცდარი; or - ან, შეამოწმებს თუ რაღაცა ორიცე ჭეშმარიტია ან მცდარი
print(True and False) # -> False
print(False and True) # -> False
print(False and False) # -> False
print(True and True) # -> True
print(True or False) # -> True
print(False or True) # -> True
print(False or False) # -> False
print(True or True) # -> True
print("")

#5
print(5==5 and 5==5)
print(5==5 or 5==5)
print(5<5 and 5>5)
print(5<5 and 5>=5)
print("")

#6
num = int(input("Write down num: "))
print(num>5)
print("")

#7
name = str(input("Write down name: "))
print(name=="Job")
print("")

#8
age = int("Write down age: ")
print(age>=18)