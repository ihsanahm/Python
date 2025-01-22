class Student:
    str="Safer"
    # defualt constoctor
    def __init__(self):
       self.str

    # peramiterized constactor
    def __init__(this, fullName):
        print("Adding a student in database ")
        this.name=fullName

s1=Student("Ihsan")
print(s1.name)
s2=Student()
print(s2.str)