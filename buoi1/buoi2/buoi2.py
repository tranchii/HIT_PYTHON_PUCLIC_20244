#a= "mystring"
#b=5
#print(a+str(b))
#print(a)
#print(a[0])
#print(a[0:6])
#sliced_string = a[0:6]
#print("len(sliced_string)=",len(sliced_string))
# print(type(a),a, sep="\n")
#
#a=" i love python"
#print("truoc khi thay doi",a)
#a[0]='Y'
#print("sau khi thay doi",a)
#my_list= [1,2,3 ,'helo']
#print ("my_list", my_list)
#print ("Type:", type(my_list))
#print("my_list[0]",my_list[0])
#print("my_list[1:3]=", my_list[1:3])
#print("my_list[1:4]",my_list[1:4])
# toan tu nhan dang
#a=5
#b=6
# if<expr> :
#<statement> doan code chay khi thụt lề
# for i in range(0,10,1):
#     print(i, end='')
# a=0
# while a<10 :
#     print(a, end='\t')
#     a+=1   
#     if a==5:
def la_so_armstrong_3_chu_so(num):
    tong = 0
    temp = num
    while temp > 0:
        chu_so = temp % 10
        tong += chu_so ** 3
        temp //= 10
    return tong == num

n = int(input("Nhap vao mot so nguyen duong n: "))

print("Cac so Armstrong bac 3 tu 1 den", n, "la:")
for i in range(1, n + 1):
    if la_so_armstrong_3_chu_so(i):
        print(i)
