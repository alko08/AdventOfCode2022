with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    lineIn = ""

    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        array1 = []
        array2 = []
        found1 = False
        found2 = False

        spot = 0
        for c in lineIn:
            # --- First Strategy ---
            equal = False
            if spot > 3 and not found1:
                for i in range(0, 4):  # Compare all chars in array
                    for j in range(i+1, 4):
                        if equal or array1[i] == array1[j]:
                            equal = True
                            break
                if not equal:  # If they are all different, found answer!
                    found1 = True
                    answer1 = spot
                else:  # Else move elements down and get new char
                    for i in range(0, 3):
                        array1[i] = array1[i + 1]
                    array1[3] = c
            elif spot <= 3:  # Else fill array with 4 elements
                array1.append(c)

            # --- Second Strategy ---
            equal = False
            if spot > 13 and not found2:
                for i in range(0, 14):  # Compare all chars in array
                    for j in range(i+1, 14):
                        if equal or array2[i] == array2[j]:
                            equal = True
                            break
                if not equal:  # If they are all different, found answer!
                    found2 = True
                    answer2 = spot
                else:  # Else move elements down and get new char
                    for i in range(0, 13):
                        array2[i] = array2[i + 1]
                    array2[13] = c
            elif spot <= 13:  # Else fill array with 14 elements
                array2.append(c)

            # Increase spot by one or break if found both spots
            if not found1 or not found2:
                spot += 1
            else:
                break

        # --- Read next line ---
        line = f.readline()

    # Print Results!
    print("First Strategy: " + str(answer1))
    print("Second Strategy: " + str(answer2))
