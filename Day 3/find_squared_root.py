"""
Finding Squared Root by Newton's Method
"""

def find_squared_root(a):
    EPSILON = 0.000001
    x_0 = a 
    n = 0 

    root = x**2 - x_0
    while (1):
        count = count + 1

        root = 0.5 * (num + (a / num))

        if(abs(root - a) < EPSILON):
            break

        a = root

    return root


print(find_squared_root(327))



