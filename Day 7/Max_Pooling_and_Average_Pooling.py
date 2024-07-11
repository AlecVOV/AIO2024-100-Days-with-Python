def max_pooling(mat_a, pool_size, stride):
    # Resultant matrix after max pooling
    pooled_matrix = []

    # Iterate through the matrix with the given stride
    for i in range(0, len(mat_a) - pool_size + 1, stride):
        row = []
        for j in range(0, len(mat_a[0]) - pool_size + 1, stride):
            # Extract the pooling window
            pooling_window = [mat_a[x][y] for x in range(i, i + pool_size) for y in range(j, j + pool_size)]
            # Find the maximum value in the pooling window
            max_value = max(pooling_window)
            row.append(max_value)
        pooled_matrix.append(row)

    return pooled_matrix


def average_pooling(mat_a, pool_size, stride):
    # Ressultant matrix after average pooling
    pooled_matrix = []

    # Iterate through the matrix with the given stride
    for i in range(0, len(mat_a) - pool_size + 1, stride):
        row = []
        for j in range(0, len(mat_a[0]) - pool_size + 1, stride):
            # Extract the pooling window
            pooling_window = [mat_a[x][y] for x in range(i, i + pool_size) for y in range(j, j + pool_size)]

            print(pooling_window)
            # Find the average
            average_value = sum(pooling_window)/len(pooling_window)
            row.append(average_value)
        pooled_matrix.append(row)

    return pooled_matrix


def main():

    # Example input matrix
    mat_a = [
        [0, 0, 0, 4],
        [0, 4, 0, 2],
        [0, 1, 0, 2],
        [0, 3, 0, 2]
    ]

    #Create an empty pooling window
    pooling_window = [[0 for _ in range(2)] for _ in range(2)]

    # Perform max pooling
    result_1 = max_pooling(mat_a, len(pooling_window), 2)


    result_2 = average_pooling(mat_a, len(pooling_window), 2)
    
    print(result_1)
    print(result_2)

main()
