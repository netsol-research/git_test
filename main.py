from typing import List

def add_numbers(numbers: List[float]) -> float:
    return sum(numbers)

def sort_list(unsorted_list: List[float]) -> List[float]:
    return sorted(unsorted_list)

if __name__ == "__main__":
    n = [2, 3, 5.2, 1]
    print("Sum:", add_numbers(n))        
    print("Sorted:", sort_list(n))       
