def find_highest(input_file):
    file1 = open(input_file, 'r')
    lines = file1.readlines()

    highest = 0
    current = 0

    for line in lines:
        if line == "\n":
            if current > highest:
                highest = current
            current = 0
        else:
            current += int(line)
    return highest


def top_three(input_file):
    file1 = open(input_file, 'r')
    lines = file1.readlines()

    tops = [0, 0, 0]
    current = 0

    for line in lines:
        if line == "\n":
            if current > tops[0]:
                tops[2] = tops[1]
                tops[1] = tops[0]
                tops[0] = current
            elif current > tops[1]:
                tops[2] = tops[1]
                tops[1] = current
            elif current > tops[2]:
                tops[2] = current
            current = 0
        else:
            current += int(line)
    return tops[0] + tops[1] + tops[2]


if __name__ == '__main__':
    # result = find_highest("input.txt")
    result = top_three("input.txt")
    print(result)
