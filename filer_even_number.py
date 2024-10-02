import random

s = int(input("Enter starting of the range: "))
e = int(input("enter ending of the range: "))
random_numbers = [random.randint(1, 100) for _ in range(s, e+1)]