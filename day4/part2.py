def convolution2d(array):
    filter = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sum = 0;
    m = len(array)
    n = len(array[0])
    new_array = [[0 for _ in range(n+2)] for _ in range(m+2)]
    ret_array = [[0 for _ in range(n)] for _ in range(m)]
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
            ret_array[i-1][j-1] = temp_sum  
    return ret_array

def print_2d_array(array):
    for line in array:
        print(line)
    
    

if __name__ == '__main__':

    # get input
    input = []
    with open('inputs/day4_input.txt', 'r') as file:
        for line in file:
            input.append(line.strip())



    forklifts = [list(map(lambda x: 1 if x == '@' else 0, l)) for l in input]

    summed = convolution2d(forklifts)

    m = len(forklifts)
    n = len(forklifts[0])

    pot = [[0 for _ in range(n)] for _ in range(m)]

    final_sum = 0

    changed = True

    while(changed): # when nothing in the array changes, stop
        changed = False

        for i in range(len(summed)):
            for j in range(len(summed[0])):
                neighbour_array = [] # check possible neighbours neighbourhood
                if i>0:
                    neighbour_array.append((-1,0))
                if j>0:
                    neighbour_array.append((0,-1))
                if i>0 and j>0:
                    neighbour_array.append((-1,-1))
                if i<m-1:
                    neighbour_array.append((1,0))   
                    if j>0:
                        neighbour_array.append((1,-1))
                if j<n-1:
                    neighbour_array.append((0,1))
                    if i>0:
                        neighbour_array.append((-1,1))
                if i<m-1 and j<n-1:
                    neighbour_array.append((1,1))

                if forklifts[i][j] >= 1: # make sure there is a forklift
                        if summed[i][j] < 4: # if this has less than 4 neighbour
                            changed = True
                            # print("Remove ", forklifts[i][j], " rolls from index ", i, j)
                            # print("neighbour array: ", neighbour_array)
                            final_sum += 1 # we can knock this one down
                            forklifts[i][j] = 0
                            summed[i][j] = 0
                            for k,l in neighbour_array:
                                if (k != 0 or l != 0) and forklifts[i+k][j+l] >= 1:
                                    summed[i+k][j+l] -= 1 # remove a neighbour
                        
                # print("Iteration ", i*n+j)
                # if i*n+j < 50: print_2d_array(summed)
    
    print(final_sum)
