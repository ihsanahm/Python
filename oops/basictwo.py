class  Car:
    def __init__(self,model,color,year,is_forsel):
        self.model=model
        self.color=color
        self.year=year
        self.is_forsel=is_forsel
    def drive():
        print("You can drive the car")
    def stop():
        print("You stop the car")
    def disception(self):
        print(f"{self.model},{self.year},{self.color},{self.is_forsel}")

car1=Car("ABC","Red",1996,True)
car1.disception()



    