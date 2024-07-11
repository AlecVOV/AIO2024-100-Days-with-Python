import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        sum_of_x_and_y = self.x**2 + self.y**2
        result = math.sqrt(sum_of_x_and_y)
        print(f"Khoảng cách từ O(0,0) đến ({self.x},{self.y}) là {result}")

    
    def display_info(self):
        print(f"Tọa độ điểm x là {self.x}, tọa độ điểm y là {self.y}")

    

A_point = Point(1, 2)
B_point = Point(4, 5)
A_point.distance_to_origin()
B_point.distance_to_origin()
