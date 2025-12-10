def apply_rotation(position, rotation):
    if rotation.startswith('L'):
        return  (position - int(rotation[1:])) % 100
    else:
        return (position + int(rotation[1:])) % 100
    

if __name__ == '__main__':

    # get input

    input = []
    with open('inputs/day1_input.txt', 'r') as file:
        for line in file:
            input.append(line.strip())

    # set initial position
    position = 50

    # total counts of 0
    total = 0

    # apply rotations
    for rotation in input:
        position = apply_rotation(position, rotation)
        if position == 0:
            total += 1

    # print total
    print(total)