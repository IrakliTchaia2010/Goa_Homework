print("Part 1:")
print("")

#1
name=str(input("Name: "))
print(name.lower())
print("")

#2
color=str(input("Color: "))
print(color.upper())
print("")

#3
city=str(input("City: "))
print(city.capitalize())
print("")

#4
email=str("student@university.ge")
print(email.find("@"))
print("")

#5
word=str("Programming")
print(word.index("r"))
print("")

#6
sentence=str("მე მიყვარს ვაშლი და მსხალი.")
print(sentence.find("ბანანი"))
print("")

#7
info=str("Error 404: Page not found")
print(info.find("404"))
print("")

#8
url=str("https://www.google.com")
print(url.startswith("https://"))
print("")

#9
phone=str("+995555123456")
print(phone.startswith("+995"))
print("")

#10
filename=str("document.pdf")
print(filename.endswith(".pdf"))
print("")

#11
sent=str(input("Insert sentence: "))
print(sent.endswith("?"))
print("")

#12
word=str("abracadabra")
print(word.count("a"))
print("")

#13
data=str("100110101011")
print(data.count("1"))
print("")

#14
products=str("პური,რძე,კვერცხი,ყველი")
print(products.split("რძე"))
print("")

#15 (ეგ არ გვისწავლია)
hello=str("hello world")
print(len(hello))
print("")
print("")

print("Part 2:")
print("")

#:::16::::
log_record=str(">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent")

#16.1
print("არის ეს ერორის ლოგი? -",log_record.startswith(">ERROR:"))
print("")

#16.2
print(log_record.endswith("#urgent"))
print("")

#16.3
print(log_record.count("#backup"))
print("")

#16.4
print(log_record.find("failed"))
print("")

#16.5
print(log_record.index("@"))
print("")

#16.6:
words_list=[">ERROR:","user","MARIAM@COMPANY.GE","failed","to","load","the","backup","file.","#backup","#Server","#backup","#urgent"]

#16.6.1
print(words_list[7].upper())
print("")

#16.6.2 + 16.6.3
print(words_list[2].lower())
print(words_list[2].lower().capitalize().split("@"))
print("")