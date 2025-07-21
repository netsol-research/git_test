def add_numbers(a_list):
 sum = 0
 for num in a_list:
  sum += num
 return sum


def sort_list(unsorted_list:list):
 unsorted_list.sort()
 return unsorted_list


if __name__ == "__main__":
 print(add_numbers([2,3,4]))
 print(sort_list([2,3,5.2,1]))

 