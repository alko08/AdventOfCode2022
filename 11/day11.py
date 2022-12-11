def monkey_math(monkey_in, value, divide):
    # Instead of taking in input, the values have been hard coded to simplify things.
    throw = 0

    if monkey_in == 0:
        value = value * 19
        if divide:
            value = int(value/3)

        if value % 17 == 0:
            throw = 2
        else:
            throw = 7
    elif monkey_in == 1:
        value = value + 2
        if divide:
            value = int(value/3)

        if value % 19 == 0:
            throw = 7
        else:
            throw = 0
    elif monkey_in == 2:
        value = value + 7
        if divide:
            value = int(value/3)

        if value % 7 == 0:
            throw = 4
        else:
            throw = 3
    elif monkey_in == 3:
        value = value + 1
        if divide:
            value = int(value/3)

        if value % 11 == 0:
            throw = 6
        else:
            throw = 4
    elif monkey_in == 4:
        value = value * 5
        if divide:
            value = int(value/3)

        if value % 13 == 0:
            throw = 6
        else:
            throw = 5
    elif monkey_in == 5:
        value = value + 5
        if divide:
            value = int(value/3)

        if value % 3 == 0:
            throw = 1
        else:
            throw = 0
    elif monkey_in == 6:
        value = value * value
        if divide:
            value = int(value/3)

        if value % 5 == 0:
            throw = 5
        else:
            throw = 1
    elif monkey_in == 7:
        value = value + 3
        if divide:
            value = int(value/3)

        if value % 2 == 0:
            throw = 2
        else:
            throw = 3

    # Due to the mod operations being preformed we don't need to go above this value
    value = value % (17 * 19 * 7 * 11 * 13 * 3 * 5 * 2)
    return [throw, value]


with open('data.txt') as f:  # Take in data.txt as an input file
    items = [[83, 97, 95, 67], [71, 70, 79, 88, 56, 70], [98, 51, 51, 63, 80, 85, 84, 95],
             [77, 90, 82, 80, 79], [68], [60, 94], [81, 51, 85], [98, 81, 63, 65, 84, 71, 84]]
    monkeys = [0] * 8

    # --- First Strategy --- Check if one range contains other range
    for rounds in range(20):
        for monkey in range(8):
            length = len(items[monkey])
            monkeys[monkey] += length
            for i in range(length):
                temp = monkey_math(monkey, items[monkey].pop(), True)
                items[temp[0]].append(temp[1])

    monkeys.sort(reverse=True)
    answer = monkeys[0] * monkeys[1]

    # --- Second Strategy --- Check if either range's lowest value is within the other range
    items = [[83, 97, 95, 67], [71, 70, 79, 88, 56, 70], [98, 51, 51, 63, 80, 85, 84, 95],
             [77, 90, 82, 80, 79], [68], [60, 94], [81, 51, 85], [98, 81, 63, 65, 84, 71, 84]]
    monkeys = [0] * 8

    for rounds in range(10000):
        for monkey in range(8):
            length = len(items[monkey])
            monkeys[monkey] += length
            for i in range(length):
                temp = monkey_math(monkey, items[monkey].pop(), False)
                items[temp[0]].append(temp[1])

    monkeys.sort(reverse=True)
    answer2 = monkeys[0] * monkeys[1]

    # Print Results!
    print("First Strategy: " + str(answer))  # 10605
    print("Second Strategy: " + str(answer2))  # 25712998901
