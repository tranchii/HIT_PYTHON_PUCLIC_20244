import random
n = int(input("Nhap n: "))
l = ["CNTT", "KHMT", "KTPM", "HTTT"]
my_dict = dict()
for i in range(n):
    my_dict[f"Account{i}"]= {
        "Username": + 20236000 + i + 1 , "Password": random.choice(l) + str(20236000 + 1 + i)
    }
print(my_dict)