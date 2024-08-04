n= int(input())
Mang=tuple(str(input()) for i in range(n))
Tuple_p=tuple(str(x) for x in Mang)
print(Tuple_p)
Dem=0
for x in Tuple_p:
    if x.isdigit():
        Dem+=1
print("tổng số phần tử là:",Dem)