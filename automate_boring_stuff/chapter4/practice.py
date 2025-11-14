#Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(input):
    to_str = ''
    if len(input) == 0:
        return to_str
    elif len(input) == 1:
        return input[0]
    elif len(input) == 2:
        return to_str + input[0] + ' and ' + input[1]
    else:
        for i in range(len(input)):
            if i == len(input) - 1:
                to_str = to_str + ' and ' + input[i]
            elif i == 0:
                to_str = to_str + input[i]
                continue
            else:
                to_str = to_str + ', ' + input[i]
        return to_str


# print(comma_code([]))
# print(comma_code(['test1']))
# print(comma_code(['test2', 'test3']))
# print(comma_code(spam))

## Coin Flip Streaks
import random
number_of_streaks = 0
for number in range(10000):
    