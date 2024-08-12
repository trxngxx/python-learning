print("Check the largest number among three numbers")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
    print("All numbers are equal")
elif a >= b and a >= c:
    print("a is the largest")
elif b >= a and b >= c:
    print("b is the largest")
else:
    print("c is the largest")
