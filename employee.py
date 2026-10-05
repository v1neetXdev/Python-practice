class Employee :
    def __init__(self , role , dep , sal):
        self.role = role
        self.dep = dep
        self.sal = sal

    def showNumber(self):
        print("Role:", self.role)
        print("Department:", self.dep)
        print("Salary:", self.sal)

class Engineer(Employee) :
    def __init__(self , name , age , role , dep , sal):
        self.name = name
        self.age = age

        super().__init__(role , dep , sal)

e = Engineer("vineet" , 18 , 'Web development ' , 'Computer Engineering' , '$1000/month')
print("Name:", e.name)
print("Age:", e.age)
e.showNumber()


