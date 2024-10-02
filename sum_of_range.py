s = int(input("Enter starting number of range: "))
e = int(input("Enter last number of range: "))
try:
    print(sum(list(range(s, e+1))))
except ValueError or TypeError:
    print("Something went wrong!!")