#2
# .append(value) - ჩაამატებს ინდექსს სიის ბოლოში
# .insert(index, value) - იგივე მაგრამ სპეციფიურ ინდექზე, ინდექსის წინ და მისი მნიშვნელობა
# .pop(index) - წაშლის რომელიმე ინდექსს

#3
arr=["A","B","C",1,2,3,1.1,2.2,3.3,True,False]
print(len(arr))
print("")

#4
include=[]
print("Inser the following 5 things to put in an array:")
arrQ1=str(input())
include.append(arrQ1)
arrQ2=str(input())
include.append(arrQ2)
arrQ3=str(input())
include.append(arrQ3)
arrQ4=str(input())
include.append(arrQ4)
arrQ5=str(input())
include.append(arrQ5)
print(include)
print("")

#5
colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop(-1)
print(colors)
print("")

#6
animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1,"monkey")
print(animals)
print("")

#7
empty=[]
print("Insert the 3 things to put in an array:")
qArr1=str(input())
empty.append(qArr1)
qArr2=str(input())
empty.append(qArr2)
qArr3=str(input())
empty.append(qArr3)
print(empty)
empty.insert(0,"Teacher")
empty.pop(-1)
print(empty)