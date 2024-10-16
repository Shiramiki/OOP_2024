from Vehicle import vehicle

class Car(vehicle):
    def __init__(self, color, winterTyres:bool):
        super().__init__(color)
        self.winterTyres = winterTyres

    def toString(self):
        super().toString()
        print(f"Has winter tires: {self.winterTyres}")


        


vehi=Car("bred", False)
vehi.toString()

