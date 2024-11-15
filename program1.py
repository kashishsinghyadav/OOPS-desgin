#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
class Circle:
    def __init__(self,r):
        self.r=r 
    def calculate_area(self):
        return 3.14*self.r*self.r 
    def calculate_perimeter(self):
        return 2*3.14*self.r 
obj=Circle(2)
print(obj.calculate_area()) 
print(obj.calculate_perimeter())