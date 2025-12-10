def get_range(range):
    tup = tuple(map(int, range.split('-')))
    tup = (tup[0], tup[1] + 1)
    return tup

def is_repetition(number):
    st = str(number)
    if (len(st)) % 2 == 1: # uneven amount of digits, not possible to be repeated
        return False;
    elif int(st[:len(st)//2]) == int(st[len(st)//2:]): # even amount of digits, check if first half is equal to second half
        return True;
    else:
        return False;
    

if __name__ == '__main__':

    # get input
    input = []
    with open('inputs/day2_input.txt', 'r') as file:
        for line in file:
            input = input + (line.strip().split(','))

    # set sum
    sum = 0

    # add up the invalid ids
    for rng in map(get_range, input):
        for nr in range(*rng):
            if is_repetition(nr):
                sum += nr
    print(sum)