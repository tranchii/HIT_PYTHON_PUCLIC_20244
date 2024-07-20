#Phan a:
a=int(input("nhap mot so nguyen: "))
tongchuso=0
while a>0:
    chusocuoi =a%10
    tongchuso+=chusocuoi
    a//=10
print("tong cac chu so cua so nguyen la:",tongchuso)

#Phan b:
n=int(input("n= "))
tongcacuoc=0
for i in range(1,n):
    if n %  i ==0:
        tongcacuoc+=i
print("tong cac uoc cua n la:",tongcacuoc)

#phan c:
b1= int(input("so nguyen 1: "))
b2= int(input("so nguyen 2: "))
b3= int(input("so nguyen 3: "))
if b1+b2>b3 and b2+b3>b1 and b3+b1>b2 :
    print("la tam giac")
    if b1==b2 or b2==b3 or b3==b1 :
        if b1==b2 and b2==b3 and b3==b1 :
            print("la tam giac deu")
        else :
            print("la tam giac can")
    elif b1*b1+b2*b2==b3*b3 or b2*b2+b3*b3==b1*b1 or b3*b3+b1*b1==b2*b2 :
        print("la tam giac vuong")
    elif b1*b1+b2*b2>b3*b3 or b2*b2+b3*b3>b1*b1 or b3*b3+b1*b1>b2*b2 :
        print("la tam giac nhon")
    else :
        print("la tam giac tu")
else :
    print("khong la tam giac")