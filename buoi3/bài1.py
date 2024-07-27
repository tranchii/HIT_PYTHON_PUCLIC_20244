n = int(input("Nhap N: "))
my_list = []
my_list = [int(input(f'a[{i}] = ')) for i in range(n)]
print(my_list)
x = int(input("Nhap X: "))
cnt = 0
for a in my_list:
    if a == x:
        cnt += 1
print(f"So lan {x} xuat hien trong list la:", cnt)
my_list[2:8] = [8, 5, 4, 0, 1, 3]
print("List sau khi thay the phan tu la: ", my_list)
print("Max: ", max(my_list))
print("Min: ", min(my_list))
y = int(input("Nhap y: "))
my_list.insert(0, y)
print("List sau khi chen: ", my_list)
if sorted(my_list, reverse = False) == my_list:
    print("Tang")
elif sorted(my_list, reverse = True) == my_list:
    print("Giam")
else :
    print("No")
my_list1 = [sum(my_list[0:i + 1]) for i in range(n + 1)]
print("my_list1 = ", my_list1)
my_list2 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print("Sap xep tang dan theo gia tri: ", sorted(my_list2, reverse = False))
my_list2 = [abs(i) for i in my_list2]
print("Sap xep tang dan theo gia tri tuyet doi: ",sorted(my_list2, reverse= False))