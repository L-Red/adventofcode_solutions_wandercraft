def apply_rotation(position, rotation):
    if rotation.startswith('L'):
        if position == 0: # we already "clicke" in the previous rotation
            return  (position - int(rotation[1:])) % 100, abs(((100 - position) + int(rotation[1:])) // 100) -1
        else:
            return  (position - int(rotation[1:])) % 100, abs(((100 - position) + int(rotation[1:])) // 100)
    else:
        return (position + int(rotation[1:])) % 100, (position + int(rotation[1:])) // 100
    

if __name__ == '__main__':

    # get input

    input = []
    with open('inputs/day1_input.txt', 'r') as file:
        for line in file:
            input.append(line.strip())

    # set initial position
    position = 50

    # total counts of 0 clicks
    total = 0

    # apply rotations
    for rotation in input:
        position, clicks = apply_rotation(position, rotation)
        if clicks > 0:
            print("At rotation", rotation, "position", position, "clicks", clicks)
            total += clicks

    # print total
    print(total)