"""wrapping data and methods together in a class restricting direct access to some data
user interact through method instead directly changing data"""

#without encapsulation
class employee:
    def __init__(self):
        self.salary = 6000

emp = employee()
emp.salary = -1000  # here i have changed the salry 
print(emp.salary) 


#with encapsulation
class employee:
    def __init__(self):
        self.__salary = 6000   #__this to make private

    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary

    def get_slary(self):
        return self.__salary
    
emp = employee()
emp.set_salary(-100)
print(emp.get_slary())

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
    print(result)          #here we use getter
print(emp.get_slary())


#example bank
class bank:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            print("insufficient balance")

    def show_balance(self):
        print("balance",self.__balance)

acc1 = bank(1000)
result=acc1.withdraw(200)
print(result)
