class Student:
    # defualt constoctor
    def __init__(this):
       pass
    # peramiterized constactor
    def __init__(this, fullName):
        print("Adding a student in database ")
        this.name=fullName

s1=Student("Ihsan")
print(s1.name)