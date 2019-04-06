class Student():
    
    # propertys:
    sum_grades=0
    sum_ages=0
    sum_students=0

    # Constructor to create a new student
    def __init__(self,grade,age):
        self.grade=grade
        self.age=age

        # sums all grades,ages,and numbers of students each time i will create a new object in main
        Student.sum_grades+=grade
        Student.sum_ages+=age
        Student.sum_students+=1

    # Function as print tahe grade and age of the student
    def show(self):
        print("grade: {}\nage: {}\n".format(self.grade,self.age))
    
    
    # Function in class as print all Sums 
    @classmethod
    def Description(class_level):
        print("sum of grades is: {}".format(class_level.sum_grades))
        print("sum of ages is: {}".format(class_level.sum_ages))
        print("sum of students is: {}".format(class_level.sum_students))



#Main:

print("\nStart calculation:\n------------------")
Student.Description()
print("\n")

s1=Student(80,20)
print("Student number (1):\n-------------------")
Student.show(s1)

s2=Student(90,21)
print("Student number (2):\n-------------------")
Student.show(s2)

s3=Student(95,19)
print("Student number (3):\n-------------------")
Student.show(s3)

s4=Student(70,23)
print("Student number (4):\n-------------------")
Student.show(s4)

print("End calculation:\n________________")
Student.Description()
        
        
