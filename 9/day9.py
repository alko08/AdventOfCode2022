with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    lineIn = ""

    array = [[0] * 400 for i in range(400)]

    HeadX = 0
    HeadY = 0
    TailX = 0
    TailY = 0
    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        temp = lineIn.split(' ')
        if temp[0] == 'R':
            HeadX += int(temp[1])
        elif temp[0] == 'L':
            HeadX -= int(temp[1])
        elif temp[0] == 'U':
            HeadY += int(temp[1])
        elif temp[0] == 'D':
            HeadY -= int(temp[1])

        # --- First Strategy ---

        # --- Second Strategy ---

        # --- Read next line ---
        line = f.readline()

    # Print Results!
    print("First Strategy: " + str(minX) + " " + str(maxX))
    print("Second Strategy: " + str(minY) + " " + str(maxY))
