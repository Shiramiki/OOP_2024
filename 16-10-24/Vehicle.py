class vehicle:
    def __init__(self, color:str):
        self.color = color

    def getColor(self):
        return self.color

    def toString(self):
        print(f"This vehicle is {self.getColor()}")

    
pajaro = vehicle("red")
pajaro.toString()