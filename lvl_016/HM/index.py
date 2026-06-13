#2
#slicing არის ნებისმიერი ინდექსის ამოღება

#3
fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])
print("")

#4
numbers = [10, 20, 30, 40, 50]
numbers[1]=25
print(numbers)
print("")

#5
colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]
print(colors[0:4])
print("")

#6
animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1]="გემი"
print(animals)
print("")

#7
colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
numCol=input("Enter num: ")
newCCol=input("Enter new color: ")
colors[int(numCol)]=newCCol
print(colors)
print("")

#8
numbers_step = [5, 10, 15, 20, 25, 30, 35, 40]
print(numbers_step[0:-1:2])
print("")

#9
fruits = ["ვაშლი", "მსხალი", "ატამი", "ბალი", "ყურძენი", "ბანანი", "ფორთოხალი"]
print(fruits[2:5])
print("")

#10
mixed_nums = [12, 45, 8, 33, 91, 24, 10, 77]
for i in mixed_nums:
    if i%2==0:
        print(i)
print("")