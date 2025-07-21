def add_numbers(x, y, z):
    return x + y + z

def add_multiple_number():
    numbers = [2, 3, 5, 10]
    result = sum(numbers)
    return result

def sort_list(unsorted_list: list):
    unsorted_list.sort()
    return unsorted_list


print(add_numbers(2, 3, 4))
print(sort_list([2, 3, 5.2, 1]))
print(add_multiple_number()) 
