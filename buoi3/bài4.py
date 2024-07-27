hoten = input("Nhap ho va ten: ")
a = list(hoten)
b = []
for i in range(len(a)):
    if not(a[i] == ' ' and (a[i - 1] == " " or i == 0)):
        b.append(a[i])
hoten = "".join(b)
hoten = hoten.title()
print("Sau khi dinh dang la: ", hoten)