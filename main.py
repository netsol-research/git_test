from typing import List

def add_numbers(num_list:List):
    sum = 0
    for num in num_list:
      sum = sum + num
    return sum


def sort_list(unsorted_list:List):
 List.sort(unsorted_list)
 return unsorted_list


if __name__ == "__main__":
    num_list = [2,3,5.2,1]
    print(add_numbers(num_list))
    print(sort_list(num_list))

 