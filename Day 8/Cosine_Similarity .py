import math

def multiply_two_vectors(vecA, vecB):
    multiplication = sum(a * b for a, b in zip(vecA, vecB))
    return multiplication

def calculate_vector_length(vector):
    total_sum = 0
    for element in vector:
        total_sum += element**2 
    length_of_vector = math.sqrt(total_sum)

    return length_of_vector

def cosine_similarity():
    vectorA = [1, 2]
    vectorB = [4, 5]

    multiplication = multiply_two_vectors(vectorA, vectorB)
    vecA = calculate_vector_length(vectorA)
    vecB = calculate_vector_length(vectorB)

    consine_similarity_result = multiplication / (vecA * vecB)
    print(consine_similarity_result)

cosine_similarity()
