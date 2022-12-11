def find_next_dir(file, loc):
    # Recurse down to current location directory
    temp_file = file
    for spot in loc[:-1]:
        temp_file = temp_file[spot]

    # Find next directory in location (assume it exists)
    for spot in range(loc[-1], len(temp_file)):
        if type(temp_file[spot]) is list:
            loc[-1] = spot  # Set last location to directory spot
            break
    loc.append(0)  # Enter directory
    return loc


def add_dir(file, loc):
    if len(loc) == 1:  # Base case, add empty directory
        file = file + [[]]
    else:  # Else not at location, recurse to location
        spot = loc[0]
        file[spot] = add_dir(file[spot], loc[1:])
    return file


def add_file(file, loc, size):
    if len(loc) == 1:  # Base case, add file with size "size"
        file = file + [size]
    else:  # Else not at location, recurse to location
        spot = loc[0]
        file[spot] = add_file(file[spot], loc[1:], size)
    return file


def less_100000(file, total):
    count = 0  # directory size
    for size in file:  # Check all children files & directory
        if type(size) is list:  # If directory recurse on it
            temp_count = less_100000(size, 0)
            count += temp_count[0]
            total += temp_count[1]
        else:  # If file add to size
            count += size

    if count <= 100000:  # If size <= 1,000,000 add to total count
        total += count
    return count, total


def smallest_dir(file, small_dir, desired_size):
    count = 0  # directory size
    for size in file:  # Check all children files & directory
        if type(size) is list:  # If directory recurse on it
            temp_count = smallest_dir(size, small_dir, desired_size)
            count += temp_count[0]
            small_dir = temp_count[1]
        else:
            count += size

    # If current size is > then desired size, but < the smallest fitting file found
    # Change the smallest file to current file (size)
    if desired_size < count < small_dir:
        small_dir = count
    return count, small_dir


with open('data.txt') as f:  # Take in data.txt as an input file
    lineIn = ""
    files = []
    location = [0]

    f.readline()  # ignore first line
    line = f.readline()
    while line:  # Read each line separately, until no more lines to read.
        # --- Do math on input ---
        lineIn = line.strip()

        # Convert input into two array of ints
        temp = lineIn.split(' ')
        if temp[0] == '$':
            if temp[1] == "cd" and temp[2] == "..":
                location.pop()  # Exit current dir
                location[-1] += 1
            elif temp[1] == "cd":
                location = find_next_dir(files, location)  # Go into next directory
            # else command = ls so do nothing
        elif temp[0] == 'dir':
            files = add_dir(files, location)  # Add directory
        else:
            files = add_file(files, location, int(temp[0]))  # Add file

        # --- First Strategy ---
        less_than = less_100000(files, 0)
        answer = less_than[1]  # total size of all files <= 1,000,000

        # --- Second Strategy ---
        answer2 = 30000000 - 70000000 + less_than[0]
        answer2 = smallest_dir(files, 70000000, answer2)[1]   # smallest file fitting parameters

        # --- Read next line ---
        line = f.readline()

    # Print Results!
    # print(files)
    print("First Strategy: " + str(answer))  # 1367870
    print("Second Strategy: " + str(answer2))  # 549173
