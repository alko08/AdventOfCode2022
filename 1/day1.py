with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    answer3 = 0
    current = 0
    lineIn = 0

    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # print(line.strip())  # Check input is working

        # Do math on input
        if line.strip() == "":
            if current > answer:
                answer3 = answer2
                answer2 = answer
                answer = current
            elif current > answer2:
                answer3 = answer2
                answer2 = current
            elif current > answer3:
                answer3 = current

            current = 0
        else:
            # print(line)
            lineIn = int(line.strip())
            current += lineIn

        # Read next line
        line = f.readline()

    print("Top Elf: " + str(answer))
    print("Sum of Top 3: " + str(answer + answer2 + answer3))  # Print answer
