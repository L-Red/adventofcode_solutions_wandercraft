def convolution2d(array):
    filter = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sum = 0;
    m = len(array)
    n = len(array[0])
    new_array = [[0 for _ in range(n+2)] for _ in range(m+2)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            new_array[i][j] = array[i-1][j-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if new_array[i][j] == 0:
                continue
            temp_sum = 0
            for k in range(3):
                for l in range(3):
                    temp_sum += new_array[i+k-1][j+l-1] * filter[k][l]
            if temp_sum < 4:
                sum += 1
    return sum    
    
    

if __name__ == '__main__':

    # get input
    input = []
    m = 0
    with open('inputs/day4_input.txt', 'r') as file:
        for line in file:
            input.append(line.strip())

    n = len(input[0])

    forklifts = [list(map(lambda x: 1 if x == '@' else 0, l)) for l in input]

    print(convolution2d(forklifts))