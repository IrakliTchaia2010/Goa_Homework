#1
weather=input("Put in weather: ")
if weather=="მზიანია" or weather=="sunny" or weather=="Sunny":
    print("ვივარჯიშებ გარეთ")
elif weather=="მოღრუბლული" or weather=="cloudy" or weather=="Cloudy":
    print("ვივარჯიშებ გარეთ ოღონდ მოგვიანებით")
else:
    print("საერთოდ არ ვივარჯიშებ დღეს")
print("")

#2
for i in range(1,1001):
    if i==461:
        print("Found 461")
        break
    else:
        continue
print("")

#3
for i in range(1,101):
    if i%2==0:
        if i%3==0:
            if i%5==0:
                print(i)
            else:
                continue
        else:
            continue
    else:
        continue

    # if i/2 != float:
    #     if i/3 != float:
    #         if i/5 != float:
    #             print(i)
    #         else:
    #             continue
    #     else:
    #         continue
    # else:
    #     continue

    # if i==55:
    #     print(float(i/2))
    #     print(float(i/3))
    #     print(float(i/5))
    #     break
    # else:
    #     continue