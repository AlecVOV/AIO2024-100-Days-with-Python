def convolution_matrix(mat_a, mat_b):
    result = []
    for i in range(len(mat_a) - len(mat_b) + 1):
        row = []
        for j in range(len(mat_a[0]) - len(mat_b[0]) + 1):
            sum = 0
            for k in range(len(mat_b)):
                for l in range(len(mat_b[0])):
                    sum += mat_a[i+k][j+l] * mat_b[k][l]
            row.append(sum)
        result.append(row)
    return result

def main():
    mat_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    kernel_c = [
        [1, 1, 1],
        [0, 0, 0],
        [1, 1, 1]
    ]

    kernal = [
        [2, 4],
        [1, 3]
    ]

    result_matrix = convolution_matrix(mat_a, kernal)
    print(result_matrix)



main()