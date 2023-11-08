#  File: Employee.py
#  Name: Patrick Pichardo

class Employee:

    def __init__(self, **kwargs):
        self._name = kwargs.get('name')
        self._id = kwargs.get('id')
        self._salary = kwargs.get('salary')
        # setting standard objects that will be used through out this code

    @property
    def salary(self):
        return float(self._salary)      # gets salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary       # sets the salary

    @property
    def name(self):
        return self._name       # gets the name

    @property
    def id(self):
        return self._id     # gets the id

    def __str__(self):
        return f"{self.__class__.__name__}\n{self._name}, {self._id}, {self._salary}"
        # Creating the "Default" string that i will be calling through out the rest of the code until a point

############################################################

class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self._benifits = kwargs.get('benefits')
        # initalizing name, id, salary w/ employee.__init__ + creating benifits

    def cal_salary(self):
        #if benefits = health insurance then salary = base_salary * 0.9
        if self._benifits == ['health_insurance']:
            return self._salary * 0.9
        #if benefits = retired, then salary = base_salary * 0.8
        elif self._benifits == ['retirement']:
            return self._salary * 0.8
        #if benefits = health insurance and retired, then salary = base_salary * 0.7
        elif len(self._benifits) > 1:
            return self._salary * 0.7

    @property
    def benefits(self):
        return self._benifits
        # gets benifits

    @benefits.setter
    def benefits(self, benefits):
        self._benifits = benefits
        # sets benifits

    def __str__(self):
        return f"{Employee.__str__(self)}, {self._benifits}"
        # calling the default string format plus benifits


############################################################

class Manager(Employee):
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self._bonus = kwargs.get("bonus")
        # calling employee plus creating bonus

    def cal_salary(self):
        # salary = base_salary + bonus
        return float(self._salary + self._bonus)
        # gets calculated salary frmo doc

    @property
    def bonus(self):
        return self._bonus      # gets bonus

    def __str__(self):
        return f"{Employee.__str__(self)}, {self._bonus}"   # gets default string format plus bonus

############################################################

class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self._hours = kwargs.get('hours')
        # still calling employee plus creating hour

    def cal_salary(self):
        # salary = base_salary * hours
        return float(self._salary * self._hours)    # gets calculated salary for temps
  
    def __str__(self):
        return f"{Employee.__str__(self)}, {self._hours}"
        # After calling the default string we will start using this as the defult string for any thing that
        # derives from a temporary employee

############################################################

class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        Temporary_Employee.__init__(self, **kwargs)
        self._travel = kwargs.get('travel')
        # now calling temp emp instead to include hours plus travel

    def cal_salary(self):
        return float((self._salary * self._hours) + (self._travel * 1000))
        # gets calculated salary for consultant

    def __str__(self):
        return f"{Temporary_Employee.__str__(self)}, {self._travel}"
        # now calling temp emp default string to include hours + travel

############################################################

class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)
        # calling consultant and manager for all the necessary properties

    # Consultant Managers are a type of Consultant and a type of Manager. 
    def cal_salary(self):
        # salary = (base_salary * hours) + (trips * 1000) + bonus
        return float((self._salary * self._hours) + (self._travel * 1000) + self._bonus)
        # gets calculated salary for consultant managers

    def __str__(self):
        return f"{Consultant.__str__(self)}, {Manager.__str__(self)}"
        # since we need the string from both the consultant and manager, we just call both

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()
