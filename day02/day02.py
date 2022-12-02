def hand_score(input_file):
    file1 = open(input_file, 'r')
    lines = file1.readlines()

    score = 0

    for line in lines:
        enemy = decode_hand(line[0:1])
        friend = decode_hand(line[2:3])

        winner = 0
        if enemy == friend:
            winner = 3
        elif (enemy % 3) + 1 == friend:
            winner = 6

        score = score + friend + winner

    return score


def win_score(input_file):
    file1 = open(input_file, 'r')
    lines = file1.readlines()

    score = 0

    for line in lines:
        enemy = decode_hand(line[0:1])
        win = decode_hand(line[2:3])

        hand = 0
        if win == 1:
            hand = enemy
        elif win == 2:
            hand = (enemy + 1) % 3
        else:
            hand = (enemy - 1) % 3

        score = score + win * 3 + hand + 1

    return score


def decode_hand(symbol):
    if symbol == "A" or symbol == "X":
        return 0
    if symbol == "B" or symbol == "Y":
        return 1
    if symbol == "C" or symbol == "Z":
        return 2


if __name__ == '__main__':
    result = win_score("input.txt")
    print(result)
