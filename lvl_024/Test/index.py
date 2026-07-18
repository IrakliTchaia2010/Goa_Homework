def math(num1,num2):
    return num1+num2
math(1,1)

def numcheck(totalnum):
    if totalnum%2==0:
        print("რიცხვი ლუწია")
    elif totalnum%1==0:
        print("რიცხვი კენტია")
    else:
        print("INVALID")
    return totalnum
numcheck(math(1,1))
print("")