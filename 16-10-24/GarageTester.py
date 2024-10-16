from Garage import Garage
from Truck import Truck


class Garage_Tester(Garage):
    def __init__(self):
        super().__init__()

    def getExample(self):
        truck = Truck('black', False)
        ourgarage = Garage()
        ourgarage.setVehicle(truck)
        return ourgarage.toString()


if __name__ == '__main__':
    print(Garage_Tester().getExample())

	
 