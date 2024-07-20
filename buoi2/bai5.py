n = int(input("Nhap vao mot so nguyen duong n: "))
def la_so_armstrong_3_chu_so(n):
    tong = 0
    temp = n
    while temp > 0:
        chu_so = temp % 10
        tong += chu_so ** 3
        temp //= 10
    return tong == n
print("Cac so Armstrong bac 3 tu 1 den", n, "la:")
for i in range(1, n + 1):
    if la_so_armstrong_3_chu_so(i):
        print(i)



