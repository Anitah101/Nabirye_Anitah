class Person:
     def __init__(self,first_name,last_name,age):
         self.first_name=first_name
         self.last_name=last_name
         self.age=age
     
     def display_info(self):       #Method displays all object attributes
         print(f"First Name:{self.first_name}")
         print(f"Last Name:{self.last_name}")
         print(f"Age:{self.age}")
         
class Student(Person):
    def __init__(self, first_name, last_name, age,reg_number,course):
        super().__init__(first_name, last_name, age)  
        self.reg_number=reg_number
        self.course=course
    
    def display_info(self):
        super().display_info() 
        print(f"Registration NUmber:{self.reg_number}")
        print(f"Course:{self.course}") 
        print("____________________")         
        
        
class Lecturer(Person):
    def __init__(self, first_name, last_name, age,ID,title):
        super().__init__(first_name, last_name, age)  
        self.ID=ID
        self.title=title
    
    def display_info(self):
        super().display_info() 
        print(f"ID:{self.ID}")
        print(f"Title:{self.title}") 
        print("____________________") 
        
class Staff(Person):
    def __init__(self, first_name, last_name, age,ID,role):
        super().__init__(first_name, last_name, age)  
        self.ID=ID
        self.role=role
    
    def display_info(self):       
        super().display_info() 
        print(f"Staff ID:{self.ID}")
        print(f"Role:{self.role}")                        
        print("____________________")
         

student=Student("Nabirye","Anitah",21,"23/U/12826/EVE","Bachelor of Science In Software Engineering")
student.display_info()

lecturer=Lecturer("Mark","John",45,"D-004","Professor")
lecturer.display_info()

staff=Staff("Luke","David",40,"C-12","Cleaner")   
staff.display_info()   
