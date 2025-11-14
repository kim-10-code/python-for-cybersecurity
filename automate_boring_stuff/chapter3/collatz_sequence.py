def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print('Enter number')
while True:
    try:
        user_input = int(input())
        collatz(user_input)

    except ValueError:
        print('Error, value must be an integer')