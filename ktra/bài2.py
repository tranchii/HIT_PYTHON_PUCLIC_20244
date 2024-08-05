x=int(input("nhập toaj độ đến đích:"))
sobuoc =0 
while x>=3 :
    x=x-3
    sobuoc=sobuoc+1
if x==2:
    x=x-2
    sobuoc=sobuoc+1
elif x==1:
    sobuoc=sobuoc+1
print("so buoc la:", sobuoc)        
