with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    lineIn = ""

    row = 0
    array = [[0] * 99 for i in range(99)]
    array1 = [[0] * 99 for i in range(99)]
    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        # Convert input into array
        for i in range(99):
            array[row][i] = int(lineIn[i])

        # --- Read next line ---
        row += 1
        line = f.readline()

    # --- First Strategy ---
    for i in range(99):  # Mark Edges as can see to start
        array1[0][i] = 1
        array1[i][0] = 1
        array1[98][i] = 1
        array1[i][98] = 1

    for i in range(1, 98):
        # Make max equal to edge tree to start
        max_left = array[i][0]
        max_right = array[i][98]
        max_top = array[0][i]
        max_bottom = array[98][i]

        for j in range(1, 98):  # Go inwards from Edge marking taller trees
            if max_left < array[i][j]:  # From left
                max_left = array[i][j]
                array1[i][j] = 1

            if max_top < array[j][i]:  # From top
                max_top = array[j][i]
                array1[j][i] = 1

            if max_right < array[i][98-j]:  # From right
                max_right = array[i][98-j]
                array1[i][98-j] = 1

            if max_bottom < array[98-j][i]:  # From bottom
                max_bottom = array[98-j][i]
                array1[98-j][i] = 1

    # --- Second Strategy ---
    for i in range(1, 98):
        for j in range(1, 98):
            left = False
            right = False
            top = False
            bottom = False
            max_height = array[i][j]
            value_left = 1
            value_right = 1
            value_top = 1
            value_bottom = 1

            for k in range(1, 98):
                if not top and i >= k and max_height > array[i - k][j]:
                    value_top += 1
                elif not top and i < k:
                    value_top -= 1
                    top = True
                else:
                    top = True

                if not bottom and i + k <= 98 and max_height > array[i + k][j]:
                    value_bottom += 1
                elif not bottom and i + k > 98:
                    value_bottom -= 1
                    bottom = True
                else:
                    bottom = True

                if not left and j >= k and max_height > array[i][j - k]:
                    value_left += 1
                elif not left and j < k:
                    value_left -= 1
                    left = True
                else:
                    left = True

                if not right and j + k <= 98 and max_height > array[i][j + k]:
                    value_right += 1
                elif not right and j + k > 98:
                    value_right -= 1
                    right = True
                else:
                    right = True

                if left and right and top and bottom:
                    break

            view = value_left * value_top * value_right * value_bottom
            if view > answer2:
                answer2 = view

    # Print Results!
    for i in array1:
        for j in i:
            answer += j

    print("First Strategy: " + str(answer))  # 1782
    print("Second Strategy: " + str(answer2))  # 474606
