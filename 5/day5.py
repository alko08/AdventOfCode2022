with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    lineIn = ""

    stacks = [['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'], ['H', 'F', 'R'], ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
              ['Q', 'H', 'P', 'B', 'F', 'W', 'G'], ['P', 'S', 'M', 'J', 'H'], ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
              ['P', 'T', 'H', 'N', 'M', 'L'], ['F', 'D', 'Q', 'R'], ['D', 'S', 'C', 'N', 'L', 'P', 'H']]

    stacks2 = [row[:] for row in stacks]  # Copy 2D array

    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        # Convert input into two array of ints
        temp = lineIn.split(' ')
        num1 = int(temp[1])
        num2 = int(temp[3])
        num3 = int(temp[5])

        # --- First Strategy ---
        for i in range(num1):
            stacks[num3-1].append(stacks[num2-1].pop())

        # --- Second Strategy ---
        temp = []
        for i in range(num1):
            temp.append(stacks2[num2-1].pop())
        temp.reverse()
        for i in range(num1):
            stacks2[num3 - 1].append(temp[i])

        # --- Read next line ---
        line = f.readline()

    # Print Results!
    print("First Strategy: ", end='')
    for s in stacks:
        print(s[-1], end='')
    print()

    print("Second Strategy: ", end='')
    for s in stacks2:
        print(s[-1], end='')
    print()
