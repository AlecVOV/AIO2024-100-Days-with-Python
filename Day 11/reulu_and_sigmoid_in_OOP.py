import math 
e = math.e

class ReLUActivateFunction:
    def __init__(self, tensor):
        self.tensor = tensor
    
    def ReLU(self):
        ReLU = list()
        for element in self.tensor:
            relu_result = max(0, element)
            ReLU.append(relu_result)
        print(ReLU)

class SigmoidActivateFunction:
    def __init__(self, tensor):
        self.tensor = tensor

    def Sigmoid(self):
        Sigmoid = list()
        for element in self.tensor:
            sigmoid_function = 1 / (1 + e**(-element))
            Sigmoid.append(sigmoid_function)
        print(Sigmoid)


tensor = [1, -5, 1.5, 2.7, -5]


result_1 = ReLUActivateFunction(tensor)
result_2 = SigmoidActivateFunction(tensor)
result_1.ReLU()
result_2.Sigmoid()

