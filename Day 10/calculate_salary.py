class Staff:
    def __init__(self, name, age, salary_per_hour, total_time):
        self.name = name
        self.age = age
        self.salary_per_hour = salary_per_hour
        self.total_time = total_time

    def calculate_bonus(self):
        salary = self.total_time * self.salary_per_hour
        if self.total_time < 100:
            bonus = 0
        elif 100 <= self.total_time < 200:
            bonus = salary * 10
        else: 
            bonus = salary * 20
        return bonus, salary
        

    def show_info(self):
        bonus, salary = self.calculate_bonus()
        if self.total_time < 100:
            print(f"Case giờ làm 99 - lương {salary} + thưởng {bonus}")
        elif 100 <= self.total_time < 200:
            print(f"Case giờ làm 199 - lương {salary} + thưởng {bonus}")
        else: 
            print(f"Case giờ làm 300 - lương {salary} + thưởng {bonus}")
        
        
        



staff_1 = Staff("Thong", 20, 1000000, 300)
staff_2 = Staff("Chi", 20, 1000000, 199)
staff_3 = Staff("Lon Thon", 20, 1000000, 99)
staff_1.show_info()
staff_2.show_info()
staff_3.show_info()

    
