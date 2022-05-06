class FlyingObject(SpaceObject):

    def __init__(self, x, y, radius, mass, speed, heading):
        super().__init__(x, y, radius, mass)
        self.speed = speed
        self.heading = heading