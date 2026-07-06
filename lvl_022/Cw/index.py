#1
fruits = ["ვაშლი", "ბანანი", "ატამი"]
fruits.insert(2,"ფორთოხალი")
print(fruits)
print("")

#2
cars = ["BMW", "Mercedes", "Audi", "Tesla"]
cars.pop(3)
print(cars)
print("")

#3
students = ["ანი", "ლუკა", "ნიკო", "ანი", "მარი"]
print(students.count("ანი"))
print("")

#4
cities = ["თბილისი", "ქუთაისი", "ბათუმი", "რუსთავი"]
cities.remove("რუსთავი")
print(cities)
print("")

#5
nums = [45, 12, 89, 3, 27]
nums.sort()
print(nums)
print("")

#6
colors = ["წითელი", "მწვანე", "ლურჯი"]
print(colors.index("მწვანე"))
print("")

#7
empty_arr=[]
print("Insert 3 favorite food:")
first_thing=str(input())
empty_arr.append(first_thing)
second_thing=str(input())
empty_arr.append(second_thing)
third_thing=str(input())
empty_arr.append(third_thing)
empty_arr.sort()
print(empty_arr)
print("")

#8
languages = ["Python", "JS", "C++", "Java"]
languages.pop(0)
print(languages)
print("")

#9
inventory = ["laptop", "mouse", "keyboard", "mouse"]
inventory.count("mouse")
for i in inventory:
    if inventory.count("mouse")>0:
        inventory.remove("mouse")
print(inventory)
print("")

#10
names = ["ნიკა", "ელენე", "გიორგი"]
print(names)
new_name=str(input("Insert new name: "))
for i in names:
    if new_name!="ელენე":
        names.append(new_name)
        break
    else:
        if names.count("ელენე")>0:
            print("ეს სახელი უკვე გვაქვს")
            break
print(names)
print("")