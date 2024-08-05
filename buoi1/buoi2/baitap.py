n= int(input('nhâp số lượng phần tử :'))
tuple1= tuple(str(input(f"nhập phần tử thứ{i+1} là: ")) for i in range(n))
tuple2= tuple(int(x)for x in tuple1)
tb= sum(tuple2)/len(tuple2)