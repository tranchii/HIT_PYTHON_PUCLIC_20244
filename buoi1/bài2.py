n = input("Nhap chuoi: ").strip()
my_dict = {}
for i in n:
    my_dict[i] = my_dict.get(i, n.count(i))
print(my_dict)