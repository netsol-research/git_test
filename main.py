from typing import List

def add_numbers(numbers: List[float]):
    return sum(numbers)

def sort_list(unsorted_list: List[float]):
    return sorted(unsorted_list)

if __name__ == "__main__":

    print(add_numbers([2, 3, 5, 10]))         
    print(sort_list([2, 3, 5.2, 1]))          
