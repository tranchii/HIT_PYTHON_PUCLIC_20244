my_set_1 ={"sv01","sv02","sv03","sv04"}
my_set_2 ={"sv05","sv06","sv07","sv08"}
print(my_set_1)
print(my_set_2)
dangkichung = my_set_1 & my_set_2
if dangkichung == set():
    print('Không cố học sinh nào đăng kí cả 2 bàn')
else:
    print('Có học sinh: ', dangkichung)
dangki1 = my_set_1 | my_set_2
print('Sinh viên đã đăng ký của cả hai bàn: ',dangki1)
dangki2 = my_set_1 - my_set_2
print('danh sách các sinh viên đã đăng ký tại bàn 1 mà không đăng ký tại bàn 2: ', dangki2)