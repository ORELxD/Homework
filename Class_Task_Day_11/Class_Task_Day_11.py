import random

# Exception if the user(cpu) inserts an incorrect age that is not between 0-120
class Non_Vaild_Age(Exception):
    def __init__(self):
        Exception.__init__(self)

# ------------------------------------------------------------------------------        
# Exception if the user(cpu) inserts an incorrect name
class Non_Vaild_Name(Exception):
    def __init__(self):
        Exception.__init__(self)

# ------------------------------------------------------------------------------
# Exception if the user(cpu) inserts an incorrect eye_color
class Non_Vaild_Eye_Color(Exception):
    def __init__(self):
        Exception.__init__(self)

# ------------------------------------------------------------------------------
# This class is contains all the information i need about the person 
class Person:
    def __init__(self,age=None, name=None, eye_color=None):
        self.age=age
        self.name=name
        self.eye_color=eye_color

# ------------------------------------------------------------------------------
# This function checks the age and has given exception if the user(random) put the wrong input
    def set_age(self,age):
        try:
            if age < 0 or age > 120 :
                raise Non_Vaild_Age()
            
        except Non_Vaild_Age:
            print("non valid age")
            age=random.randint(-20,200)
            self.set_age(age)

        except KeyboardInterrupt:  
            print("you enter Ctrl+C to Finish")
        
        except ValueError:
            print("incorrect valid")
        
        else:
            self.age=age
            print('valid age\n')

# ------------------------------------------------------------------------------
# This function checks the name and has given exception if the user(random) put the wrong input
    def set_name(self,name,NameArray): 
        try:
            if len(name) > 9 or len(name) < 3 :
                raise Non_Vaild_Name()
            
        except Non_Vaild_Name:
            print("non valid name")
            name=random.choice(NameArray)
            self.set_name(name,NameArray)

        except KeyboardInterrupt:  
            print("you enter Ctrl+C to Finish")
        
        except ValueError:
            print("incorrect valid")
        
        else:
            self.name=name
            print('valid name\n')

# ------------------------------------------------------------------------------
# This function checks the eyes color and has given exception if the user(random) put the wrong input
    def set_eye_color(self,eye_color,ColorArray):
        try:
            if eye_color != "green" and eye_color != "blue" and eye_color != "brown":
                raise Non_Vaild_Eye_Color()
            
        except Non_Vaild_Eye_Color:
            print("non valid eye_color")
            eye_color=random.choice(ColorArray)
            self.set_eye_color(eye_color,ColorArray)

        except KeyboardInterrupt:  
            print("you enter Ctrl+C to Finish")
        
        except ValueError:
            print("incorrect valid")
        
        else:
            print('valid eye_color\n')
            self.eye_color=eye_color

# -----------------------------------Main-----------------------------------------
def main():
    print("Welcome to Class Task Day 11\n___________________________")
    PersonArray=[]
    NameArray=["Tom", "li" , "Bob" , "Alice" , "Clarc" , "Adam" , "Sean"]
    ColorArray=["green", "blue" , "yellow" , "black","brown" ]
    i=0

# Create 5 Person and put each Person into array
# note:(func 'append' is push each obj to the last place in array)
    for p in range(0,5):
        PersonArray.append(Person())

# The s'user(cpu)' insert random Details(age,name,eye color) to each person
    for p in PersonArray:
        age=random.randint(-20,200)
        p.set_age(age)
        name=random.choice(NameArray)
        p.set_name(name,NameArray)
        eye_color=random.choice(ColorArray)
        p.set_eye_color(eye_color,ColorArray)

# Print each person with the random details 
    for p in PersonArray:
        i+=1
        print("Person({}):\nage: {}\nname: {}\neye color: {}\n".format(i,p.age,p.name,p.eye_color))

main()
