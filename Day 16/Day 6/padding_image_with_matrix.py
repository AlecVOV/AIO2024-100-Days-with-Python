
def convolution_matrix_with_zero_padding(mat_a, mat_b):
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
        [0, 0, 0],
        [0, 4, 0],
        [0, 1, 0]
    ]

    kernal_b = [    
        [1, 1],
        [1, 1]
    ]

    kernal_c = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

    #Create a new matrix with padding, fill it with full 0
    mat_a_output = [[0 for _ in range(len(mat_a) + 2)] for _ in range(len(mat_a[0]) + 2)]
    
    # Copy the original matrix into the center of the new matrix, in this case gonna be 4x4 into 6x6
    for i in range(len(mat_a)):
        for j in range(len(mat_a[0])):
            mat_a_output[i + 1][j + 1] = mat_a[i][j]

    result_matrix_1 = convolution_matrix_with_zero_padding(mat_a_output, kernal_b)
    print(result_matrix_1)

    result_matrix_2 = convolution_matrix_with_zero_padding(mat_a_output, kernal_c)
    print(result_matrix_2)
    
main()