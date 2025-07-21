from typing import List
def add_numbers(numbers: List):
 return sum(numbers)
 


def sort_list(unsorted_list:List):
 return sorted(unsorted_list)


if __name__ == "__main__":
 numbers_list = [2,3,1,4]
 print(add_numbers(numbers_list))
 print(sort_list(numbers_list))

 