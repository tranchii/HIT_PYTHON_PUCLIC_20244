def split_and_remove_duplicates(input_list):
    
    unique_elements = set()
    for item in input_list:
        
        for char in item:
            unique_elements.add(char)
    result_list = list(unique_elements)
    print(result_list)

input_str = input()
input_list = eval(input_str)
split_and_remove_duplicates(input_list)


