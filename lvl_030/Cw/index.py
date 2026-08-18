#1
def unusual_five():
    return len("Hello")
print(unusual_five())
print()

#2
def find_average(numbers):
    if len(numbers)<1:
        return 0
    else:
        return sum(numbers)/len(numbers)
print(find_average([1,2,3,2]))
print()