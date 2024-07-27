a= list()
k=int(input("k="))
for i in range(k):
    phan_tu = int(input(f"nhập phan tu thu {i + 1}: "))
    a.append(phan_tu)
print(a)
n=int(input("n="))
m=int(input("m="))
if n*m > k:
    print("NO")
else:
    ma_tran = []
    for i in range(n):
        hang = a[i * m: (i + 1) * m]
        ma_tran.append(hang)
    print(f"Ma trận X({n} × {m}):")
    for hang in ma_tran:
        print(hang)