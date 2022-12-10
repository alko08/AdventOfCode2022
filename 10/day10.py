with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 1
    lineIn = ""

    signals = []
    screen = [[], [], [], [], [], []]
    cycle = 1
    counter = 0
    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        # --- First Strategy ---
        if cycle % 40 == 20 and cycle <= 220:
            signals.append(cycle * answer)
        elif (cycle-1) % 40 == 0 and cycle != 1:
            counter += 1

        # --- Second Strategy ---
        if answer <= cycle % 40 <= answer+2 and counter < 6:
            screen[counter].append('#')
        elif counter < 6:
            screen[counter].append('.')

        # Check if input is addx otherwise increase cycle by 1
        temp = lineIn.split(' ')
        if temp[0] == "addx":
            temp = temp[1]
            cycle += 1

            # --- First Strategy ---
            if cycle % 40 == 20 and cycle <= 220:
                signals.append(cycle * answer)
            elif (cycle-1) % 40 == 0:
                counter += 1

            # --- Second Strategy ---
            if answer <= cycle % 40 <= answer + 2 and counter < 6:
                screen[counter].append('#')
            elif counter < 6:
                screen[counter].append('.')

            # Increase X
            answer += int(temp)
        cycle += 1

        # --- Read next line ---
        line = f.readline()

    # Print Results!
    answer = 0
    for s in signals:
        answer += s
    print("First Strategy: " + str(answer))

    print("Second Strategy: ")
    for s in screen:
        for s2 in s:
            print(s2 + " ", end='')
        print()
