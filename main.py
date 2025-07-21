from typing import List

# Add any number of numbers


def add_numbers(*args):
    return sum(args)

# Sort and return a list


def sort_list(unsorted_list: List):
    return sorted(unsorted_list)


if __name__ == "__main__":
    print(add_numbers(2, 3, 4, 5, 6))           # Output: 20
    print(sort_list([2, 3, 5.2, 1]))            # Output: [1, 2, 3, 5.2]
