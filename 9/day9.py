def pull_tail(head_x, head_y, tail_x, tail_y):
    # See if given knots are not connected
    return tail_x < head_x - 1 or tail_x > head_x + 1 or tail_y < head_y - 1 or tail_y > head_y + 1


def pull_all_tail(knots_in):
    # See if ANY knots are not connected
    connected = False
    for k in range(9):
        connected = pull_tail(knots_in[k][0], knots_in[k][1], knots_in[k + 1][0], knots_in[k + 1][1])
        if connected:
            break

    return connected


def head_to_tail(head_x, head_y, tail_x, tail_y):
    # See if given knots need to be moved, or not
    if not pull_tail(head_x, head_y, tail_x, tail_y):
        return[tail_x, tail_y]

    # Pull knots together one step horizontal/vertical
    if tail_x == head_x or tail_y == head_y:
        if tail_x < head_x:
            tail_x += 1
        elif tail_x > head_x:
            tail_x -= 1
        elif tail_y < head_y:
            tail_y += 1
        elif tail_y > head_y:
            tail_y -= 1

    # Pull knots together one step diagonal
    else:
        if tail_x < head_x:
            tail_x += 1
        elif tail_x > head_x:
            tail_x -= 1

        if tail_y < head_y:
            tail_y += 1
        elif tail_y > head_y:
            tail_y -= 1

    return [tail_x, tail_y]


with open('data.txt') as f:  # Take in data.txt as an input file
    answer = 0
    answer2 = 0
    lineIn = ""

    array = [[0] * 400 for i in range(400)]
    array2 = [[0] * 400 for j in range(400)]
    knots = [[0] * 2 for k in range(10)]

    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()
        xChange = 0
        yChange = 0

        # What value head spot needs to change
        temp = lineIn.split(' ')
        if temp[0] == 'R':
            xChange = int(temp[1])
        elif temp[0] == 'L':
            xChange = -1 * int(temp[1])
        elif temp[0] == 'U':
            yChange = int(temp[1])
        elif temp[0] == 'D':
            yChange = -1 * int(temp[1])

        # --- First & Second Strategy ---
        while xChange != 0 or yChange != 0:  # Move by one spot at a time
            if xChange > 0:
                xChange -= 1
                knots[0][0] += 1
            elif xChange < 0:
                xChange += 1
                knots[0][0] -= 1
            elif yChange > 0:
                yChange -= 1
                knots[0][1] += 1
            else:
                yChange += 1
                knots[0][1] -= 1

            # Move ALL knots until all knots are connected
            while pull_all_tail(knots):  # See if ANY knots are not connected
                for k in range(9):  # Go through all knots once, 0 to 9
                    knots[k+1] = head_to_tail(knots[k][0], knots[k][1], knots[k+1][0], knots[k+1][1])

                    # First is watching spot 1, Second is watching spot 8
                    if k == 0:
                        array[knots[1][0]+200][knots[1][1]+200] = 1
                    elif k == 8:
                        array2[knots[9][0]+200][knots[9][1]+200] = 1

        # --- Read next line ---
        line = f.readline()

    # Print Results!
    for x in array:
        for y in x:
            answer += y
    print("First Strategy: " + str(answer))  # 6243

    for x in array2:
        for y in x:
            answer2 += y
    print("Second Strategy: " + str(answer2))  # 2630
