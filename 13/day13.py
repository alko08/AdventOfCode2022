def compare_arrays_recurse(arrOne, arrTwo, intOne, intTwo):
    if intOne >= len(arrOne):
        return [False, True]
    elif intTwo >= len(arrTwo):
        return [False, False]
    else:
        value1 = arrOne[intOne]
        value2 = arrTwo[intTwo]
        list1 = type(value1) is list
        list2 = type(value2) is list
        if not list1 and not list2:
            return[value1 == value2, value1 <= value2]
        elif not list1:
            value1 = [value1]
        elif not list2:
            value2 = [value2]
        return compare_arrays(value1, value2)


def compare_arrays(arrOne, arrTwo):
    valid = True
    loop = True
    i = 0
    while loop:
        if i < len(arrOne) or i < len(arrTwo):
            temp = compare_arrays_recurse(arrOne, arrTwo, i, i)
            loop = temp[0]
            valid = temp[1]
            i += 1
        else:
            break
    return [loop, valid]


with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    lineIn = ""

    array = [[[2]], [[6]]]
    array1 = ""
    array2 = ""
    pair = False
    count = 0
    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        # Convert input into two array of ints
        if lineIn == "":
            array1 = ""
            array2 = ""
            pair = False
        elif array1 == "":
            array1 = eval(lineIn)
        else:
            array2 = eval(lineIn)
            pair = True
            count += 1

        # --- First Strategy ---
        if pair and compare_arrays(array1, array2)[1]:
            answer += count

        # --- Second Strategy ---
        if lineIn != "":
            array.append(eval(lineIn))

        # --- Read next line ---
        line = f.readline()

    # --- Second Strategy ---
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):
            if not compare_arrays(array[j], array[j+1])[1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp

    answer2 = 1
    for i in range(length):
        if array[i] == [[2]] or array[i] == [[6]]:
            answer2 *= i+1

    # Print Results!
    print("First Strategy: " + str(answer))  # 5623
    print("Second Strategy: " + str(answer2))  # 20570
