"""wrapping data and methods together in a class restricting direct access to some data
user interact through method instead directly changing data"""

#without encapsulation
# class employee:
#     def __init__(self):
#         self.salary = 6000

# emp = employee()
# emp.salary = -1000  # here i have changed the salry 
# print(emp.salary) 


#with encapsulation
# class employee:
#     def __init__(self):
#         self.__salary = 6000   #__this to make private

#     def set_salary(self,salary):
#         if salary>0:
#             self.__salary=salary

#     def get_slary(self):
#         return self.__salary
    
# emp = employee()
# emp.set_salary(-100)
# print(emp.get_slary())

class employee:
    def __init__(self):
        self.__salary = 6000   #__this to make private

    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            return "you are broke"

    def get_slary(self):
        return self.__salary
    
emp = employee()
result = emp.set_salary(-100)
if result:
    print(result)
print(emp.get_slary())