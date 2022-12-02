with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    lineIn = ""

    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # print(line.strip())  # Check input is working

        # Do math on input
        lineIn = line.strip()

        values0 = ['A', 'B', 'C']  # Rock, Paper, or Scissor for enemy
        values1 = [0, 6, 3]  # You Lose, win, or draw
        values2 = [1, 2, 3]  # You throw Rock, Paper, or Scissor
        temp = 0

        # First Strategy
        if lineIn[2] == 'X':
            answer += 1  # You throw rock
            temp = values0.index(lineIn[0]) + 2  # Calculate result
        elif lineIn[2] == 'Y':
            answer += 2  # You throw Paper
            temp = values0.index(lineIn[0]) + 1  # Calculate result
        else:
            answer += 3  # You throw Scissor
            temp = values0.index(lineIn[0])  # Calculate result

        # Prevent overflow and add result score (lose, win, or draw) to answer
        if temp > 2:
            temp -= 3
        answer += values1[temp]

        # Second Strategy
        if lineIn[2] == 'X':
            answer2 += 0  # You lose
            temp = values0.index(lineIn[0]) + 2  # Calculate what you throw
        elif lineIn[2] == 'Y':
            answer2 += 3  # You draw
            temp = values0.index(lineIn[0])  # Calculate what you throw
        else:
            answer2 += 6  # You win
            temp = values0.index(lineIn[0]) + 1  # Calculate what you throw

        # Prevent overflow and add what you throw score (Rock, Paper, or Scissor) to answer2
        if temp > 2:
            temp -= 3
        answer2 += values2[temp]

        # Read next line
        line = f.readline()

    # Results!
    print("First Strategy: " + str(answer))
    print("Second Strategy: " + str(answer2))
