n = int(input())
my_set = set(map(int, input().split()))
print(my_set)
if len(my_set) == n:
    sorted_set = sorted(my_set)
    sum = 0
    m = int(input())
    current_sum = 0
    current_subset = set()
    for number in sorted_set:
        if current_sum + number <= m:
            current_subset.add(number)
            current_sum += number
    print(current_subset)
else:
    print("không hợp lệ")  