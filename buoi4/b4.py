n = int(input())
my_set = set(map(int, input().split()))
print(my_set)
if len(my_set) == n:
    sorted_set = sorted(my_set)
    tong = 0
    m = int(input())
    sum = 0
    a = set()
    for number in sorted_set:
        if sum + number <= m:
            a.add(number)
            sum += number
    print(a)
else:
    print("không hợp lệ")  