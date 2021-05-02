class Car(object):
    def __init__(self,color,company,model,speed,matieral):
        self.color=color
        self.company=company
        self.model=model
        self.speed=speed
        self.matieral=matieral
    def setcolor(self,color):
        print("The color of the car is"+self.color)
    def setcompany(self,company):
        print("The company of the car is"+self.company)
    def setmodel(self,model):
        print("The model of the car is"+self.model)
    def setspeed(self,speed):
        print("The top speed of this vechile is"+self.speed)
    def setmatieral(self,matieral):
        print("This car is mainly made out of"+self.matieral)
car1=Car(" White"," Tesla"," S"," 180"," Steel")

print(car1.setcolor(" white"))
print(car1.setcompany("Tesla"))