import __main__
#issue resolved
def add_numbers(numbers:list):
    sum=0
    for i in range (0,len(numbers),1):
        sum=numbers[i]+sum
        
    return sum


def sort_list(unsorted_list:list):
 print (unsorted_list.sort())


if __name__ == "__main__":
 sum=[1,2,3,4,5]
 print("SUm of list=",add_numbers(sum))
 #print("Sorted list=" ,sort_list([2,3,5.2,1]))

 