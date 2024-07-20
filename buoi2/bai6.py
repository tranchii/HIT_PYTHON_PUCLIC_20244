n = int(input("Nhap  so nguyen duong n: "))
def la_so_hoan_hao(n):
    tongcacuoc = 0
    for i in range(1, n):
        if n%i == 0:
            tongcacuoc += i
    return tongcacuoc == n
print("Cac so hoan hao tu 1 den", n, "la:")
for i in range(1, n + 1):
    if la_so_hoan_hao(i):
        print(i)
