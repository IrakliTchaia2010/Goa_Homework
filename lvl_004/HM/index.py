#1
#1) input - რაღაცის შეტანა; output - რაღაცის ამოტანა

#2
# snake_case არის "_", კოდში გამატოვების ადგილის ნაშნად იხმარება კოდში, მაგ. ცვლადი "good_bye" და "good bye"

#3
something=input("Insert something: ")
if type(something)==str:
    print("String")
else:
    print("Wrong")

#4
something1="word" #string
something2="thing" #string
something3=2.4 #float
something4=1 #intiger
something5=9 #intiger

#5
str1="word"
str2="thing"
str3="what"
int1=1
int2=9
int3=129837291
float1=1.2
float2=4.5
float3=125.123132
print(type(str1))
print(type(str2))
print(type(str3))
print(type(int1))
print(type(int2))
print(type(int3))
print(type(float1))
print(type(float2))
print(type(float3))

#6
ask1=input("Insert something: ")
ask2=input("Insert something: ")
print(ask1+""+ask2)

#7
name=input("Insert name: ")
lastname=input("Insert last name: ")
age=input("Insert age: ")
height=input("Insert height: ")
weight=input("Insert weight: ")
print("Hi "+name+" "+lastname+", you are "+age+" years old, are around "+height+" tall and weight"+weight+".")