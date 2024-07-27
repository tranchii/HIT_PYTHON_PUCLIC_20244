s1 = input("s1 = ")
s2 = input("s2 = ")
print("Dao nguoc chuoi s1 la: ", s1[::-1])
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
if(1 <= a < b <= len(s2)):
    print("Chuoi s2 sau khi dao la: ", s2[:a] + s2[a:b + 1][::-1] + s2[b + 1:])
s3 = []
for i in range(0, len(s1), 2):
    s3 += s1[i] # s3.append(i)
print("Chuoi 3 sau khi xoa la: ", " ".join(s3))
s4 = []
n = max(len(s1), len(s2))
for i in range(n):
    if i < len(s1):
        s4.append(s1[i])
    if i < len(s2):
        s4.append(s2[i])
print("Chuoi 4 sau khi sap xep la: ", "".join(s4))
print("sau khi doi ki tu dau tien cua s1 va s2 ta duoc: ")
print("new s1 = ", s1.replace(s1[0], s2[0]))
print("new s2 = ", s2.replace(s2[0], s1[0]))

    