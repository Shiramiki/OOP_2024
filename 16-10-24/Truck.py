from Vehicle import vehicle

class Truck(vehicle):
    def __init__(self, color, trailer:bool):
        super().__init__(color)
        self.trailer = trailer

    def toString(self):
        super().toString()
        print(f"has trailer:{self.trailer}")


vi = Truck("Green", True)
vi.toString()