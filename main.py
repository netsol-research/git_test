from typing import List

def add_numbers(x, y):
    return x + y

def sort_list(unsorted_list: List):
    return sorted(unsorted_list)

if __name__ == "__main__":

    print(add_numbers(2, 3))
    print(sort_list([2, 3, 5.2, 1]))
