
n = int(input("How many numbers? "))


numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)



total = sum(numbers)
print("The sum is:", total)