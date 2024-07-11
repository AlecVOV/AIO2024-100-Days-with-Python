class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Employee(Person):
    def __init__(self, name, phone, annual_salary, year_of_starting_work):
        super().__init__(name, phone)
        self.annual_salary = annual_salary
        self.year_of_starting_work = year_of_starting_work



class StackEmployee:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = list()

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity
    
    def pop(self):
        if self.is_empty():
            print("Pop from an empty stack")
            return None
        popped_value = self.stack[-1]
        self.stack = [item for item in self.stack if item != popped_value] #remove that element by creating a new list and write-back all the value
        # Or we can use: self.stack.remove(popped_value)
        return popped_value 
    
    def push(self, obj):
        if self.is_full():
            print("Push to a full stack")
        else:
            self.stack.append(obj)

    def top(self):
        if self.is_empty():
            print("Top from an empty stack")
            return None
        return self.stack[-1]
    

"""------------Test-----------------"""
# Khởi tạo một số đối tượng Employee
employee1 = Employee("Alice", "123456789", 50000, 2015)
employee2 = Employee("Bob", "987654321", 60000, 2016)
employee3 = Employee("Charlie", "456123789", 70000, 2017)
employee4 = Employee("David", "789123456", 80000, 2018)
employee5 = Employee("Eve", "321654987", 90000, 2019)
employee6 = Employee("Frank", "654321987", 100000, 2020)

# Khởi tạo StackEmployee với capacity là 5
stack = StackEmployee(5)

# Kiểm tra các phương thức
stack.push(employee1)
stack.push(employee2)
stack.push(employee3)
stack.push(employee4)
stack.push(employee5)

print(stack.is_full())  # Kết quả: True
print(stack.top().name)  # Kết quả: Eve

# Thử thêm một phần tử nữa vào stack đầy sẽ gây ra lỗi
try:
    stack.push(employee6)
except IndexError as e:
    print(e)  # Kết quả: Push to a full stack

print(stack.pop().name)  # Kết quả: Eve
print(stack.is_full())  # Kết quả: False
print(stack.is_empty())  # Kết quả: False

# Lấy phần tử top hiện tại sau khi pop
print(stack.top().name)  # Kết quả: David
