#2
# .upper() - სტრინგს დიდად გადააკეთებს
# .lower() - სტრინგს პატარად გადააკეთებს
# .capitalize() - პირველ ასოს დიდად გადააკეთებს
# .find() - იპოვებს იმ რაღაცას ინდექსის ადგილში (მარტო სტრინგში იმუშავებს)
# .count() - დაითვლის რამდენჯერ არის ის ასო სტრინგში
# .len() - დაითვლის რამდენი სიმბოლო არის სტრინგში
# .endswith() - მთავრდება თუ არა რომელიმე ასოთი
# .startswith() - დაიწყება თუ არა რომელიმე ასოთი

#3
smth=str("SoMeThInG.")
print(smth.lower())
print("")

#4
email=str("Who@Gmail.com")
print(email.find("@"))
if email.find("@") > -1:
    print(email.upper())
print("")

#5
title=input(str("Insert book title: "))
print(title.capitalize())
print("")

#6
sentence=input(str("Insert sentence: "))
print("?:",sentence.count("?"))
print("a:",sentence.count("a"))
print("")

#7
newsentence=input(str("Insert sentence: "))
if newsentence == newsentence.upper():
    print("No need to make it .upper()")
else:
    print(newsentence.upper())