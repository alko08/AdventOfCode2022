with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    lineIn = ""

    line1 = ""
    line2 = ""
    line3 = ""
    counter = 0
    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # print(line.strip())  # Check input is working

        # Do math on input
        lineIn = line.strip()

        # First Strategy
        firstHalf = lineIn[0:int(len(lineIn)/2)]
        secondHalf = lineIn[int(len(lineIn)/2)::]
        # print(firstHalf + secondHalf + " = " + lineIn)

        shared = ""
        for char in firstHalf:
            if char in secondHalf and char not in shared:
                shared += char

        # print(shared)
        for char in shared:
            value = ord(char) - 38
            if value > 58:
                value -= 58
            answer += value

        # Second Strategy
        counter += 1
        if counter == 1:
            line1 = lineIn
        elif counter == 2:
            line2 = lineIn
        elif counter == 3:
            line3 = lineIn
            counter = 0

            shared = ""
            for char in line1:
                if char in line2 and char in line3:
                    shared += char
                    break

            # print(shared)
            value = ord(shared[0]) - 38
            if value > 58:
                value -= 58
            answer2 += value

        # Read next line
        line = f.readline()

    # Results!
    print("First Strategy: " + str(answer))
    print("Second Strategy: " + str(answer2))
