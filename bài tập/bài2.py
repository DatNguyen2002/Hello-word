import math
print("Nhập vào số a: ")
a = int(input())
print("Nhập vào số b: ")
b = int(input())
while True:
    if a == 0 and b == 0:
        print("Một trong hai số a và b phải khác 0: ")
        print("Nhập lại số a: ")
        a = int(input())

        print("Nhập lại số b: ")
        b = int(input())
    else:
        break
print("Nhập vào số c: ")
c = int(input())
dt = b**2 - 4 * a * c

if dt < 0:
    print("Phương trình vô nghiệm")
elif dt == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(dt))/(2*a) )
    print("x1 = ", (-(b) - math.sqrt(dt))/(2*a) )