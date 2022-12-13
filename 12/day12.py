def visit_node(curCount, curValue, rowCheck, colCheck):
    if 0 <= rowCheck <= 40 and 0 <= colCheck <= 143 and not visited[rowCheck][colCheck] \
            and array[rowCheck][colCheck] <= curValue + 1:
        queue.append([rowCheck, colCheck])
        visited[rowCheck][colCheck] = True
        steps[rowCheck][colCheck] = curCount + 1
        return rowCheck == endRow and colCheck == endCol
    else:
        return False


with open('data.txt') as f:  # Take in data.txt as an input file
    lineIn = ""
    array = [[] * 144 for i in range(41)]
    row = 0
    startRow = 0
    startCol = 0
    endRow = 0
    endCol = 0

    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        for c in lineIn:
            if c == 'S':
                array[row].append(1)
                startRow = row
                startCol = len(array[row])-1
            elif c == 'E':
                array[row].append(ord('z')-96)
                endRow = row
                endCol = len(array[row]) - 1
            else:
                array[row].append(ord(c)-96)

        # --- Read next line ---
        line = f.readline()
        row += 1

    # print(array[startRow][startCol])
    # --- First Strategy ---
    visited = [[False] * 144 for i in range(41)]
    steps = [[0] * 144 for i in range(41)]

    foundPath = False
    queue = [[startRow, startCol]]
    visited[startRow][startCol] = True
    while not foundPath and len(queue) > 0:  # BFS implementation
        temp = queue.pop(0)
        row = temp[0]
        col = temp[1]
        value = array[row][col]
        step = steps[row][col]

        foundPaths = [False, False, False, False]
        foundPaths[0] = visit_node(step, value, row - 1, col)  # Top
        foundPaths[1] = visit_node(step, value, row, col - 1)  # Left
        foundPaths[2] = visit_node(step, value, row + 1, col)  # Bottom
        foundPaths[3] = visit_node(step, value, row, col + 1)  # Right

        foundPath = foundPaths[0] or foundPaths[1] or foundPaths[2] or foundPaths[3]

    answer = steps[endRow][endCol]

    # --- Second Strategy ---
    answer2 = answer

    for startRow in range(41):
        for startCol in range(144):
            if array[startRow][startCol] == 1:
                visited = [[False] * 144 for i in range(41)]
                steps = [[0] * 144 for i in range(41)]

                foundPath = False
                queue = [[startRow, startCol]]
                visited[startRow][startCol] = True
                while not foundPath and len(queue) > 0:  # BFS implementation
                    temp = queue.pop(0)
                    row = temp[0]
                    col = temp[1]
                    value = array[row][col]
                    step = steps[row][col]
                    if step >= answer2:
                        break

                    foundPaths = [False, False, False, False]
                    foundPaths[0] = visit_node(step, value, row - 1, col)  # Top
                    foundPaths[1] = visit_node(step, value, row, col - 1)  # Left
                    foundPaths[2] = visit_node(step, value, row + 1, col)  # Bottom
                    foundPaths[3] = visit_node(step, value, row, col + 1)  # Right

                    foundPath = foundPaths[0] or foundPaths[1] or foundPaths[2] or foundPaths[3]
                if foundPath and steps[endRow][endCol] < answer2:
                    answer2 = steps[endRow][endCol]

    # Print Results!
    # for a in array:
    #     print(a)
    print("First Strategy: " + str(answer))  # 423
    print("Second Strategy: " + str(answer2))  # 416
