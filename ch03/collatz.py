def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


print("Enter number: ")
input_number = int(input())
while True:
    num = collatz(input_number)
    print('The number is ' + str(num))
    if num == 1:
        break
    input_number = num
