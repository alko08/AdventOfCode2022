with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    lineIn = ""

    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        # Convert input into two array of ints
        temp = lineIn.split(',')
        range1 = list(map(int, temp[0].split('-')))
        range2 = list(map(int, temp[1].split('-')))

        # First Strategy - Check if one range contains other range
        if ((range2[0] >= range1[0] and range2[1] <= range1[1]) or
                (range1[0] >= range2[0] and range1[1] <= range2[1])):
            answer += 1

        # Second Strategy - Check if either range's lowest value is within the other range
        if (range1[0] <= range2[0] <= range1[1]) or (range2[0] <= range1[0] <= range2[1]):
            answer2 += 1

        # --- Read next line ---
        line = f.readline()

    # Results!
    print("First Strategy: " + str(answer))
    print("Second Strategy: " + str(answer2))
