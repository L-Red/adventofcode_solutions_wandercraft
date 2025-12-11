def get_range(range):
    tup = tuple(map(int, range.split('-')))
    tup = (tup[0], tup[1] + 1)
    return tup

def get_divisors(nr):
    divs = []
    for i in range(1, int(nr**0.5) + 1): # we only need to find divisors up until sqrt(nr)
        if nr % i == 0:
            divs.append(i)
            if i != nr // i and nr // i != nr:
                divs.append(nr // i)
    if nr in divs:
        divs.remove(nr)
    return sorted(divs)

def is_repetition(number, divisors):
    st = str(number)
    if len(st) in divisors.keys():
        divs = divisors[len(st)]
    else:
        divisors[len(st)] = get_divisors(len(st))
        divs = divisors[len(st)]

    # check all permissable substrings
    for sub_len in divs:
        substrings = set()
        for i in range(len(st)//sub_len): # loop over all substrings of length sub_len
            substr = st[i*sub_len:(i+1)*sub_len]
            substrings.add(substr)
        if len(substrings) == 1: # if all substrings are the same, return True
            return True
    return False

if __name__ == '__main__':

    # get input
    input = []
    with open('inputs/day2_input.txt', 'r') as file:
        for line in file:
            input = input + (line.strip().split(','))

    # set sum
    sum = 0

    # global divisor lookup
    divisors = {}

    # add up the invalid ids
    for rng in map(get_range, input):
        for nr in range(*rng):
            if is_repetition(nr, divisors):
                sum += nr
    print(sum)