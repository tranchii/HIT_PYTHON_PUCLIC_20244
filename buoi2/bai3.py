import math

n = int(input("Nhap n: "))
result = 0
for i in range(1, 2 * n + 2, 1) :
    if i % 2 == 0:
        result += -i
    else:
        result += i
print("Cau a = ", result)

res = 0
for i in range(1, n + 1):
    res += 1/i
print("Cau b: ", res)

# Cau c
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co nghiem duy nhat x = -c/b")        
else:
    delta = b * b - 4 * a * c
    if delta == 0:
        print("Phuong trinh co nghiem kep x1 = x2 = ", -b/2 * a)
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/ 2 * a
        x2 = (-b - math.sqrt(delta))/ 2 * a
        print("Phuong trinh co hai nghiem phan biet x1 = ", x1," x2 = ", x2, sep = " ")
    else:
        print("Phuong trinh vo nghiem")