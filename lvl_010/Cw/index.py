#1
for i in range(11):
    print(i)
print("")

#2
for i in range(0,101,2):
    print(i)
print("")

#3
name=input(str("Put in your name: "))
if name=="Peter" or name=="peter":
    print("გაუმარჯოს პეტრე")
elif name=="Peter Griffin" or name=="peter griffin":
    print("Hey Lois! I'm in some kid's Python file for their homework!")
else:
    print("შენ არ ხარ პეტრე")