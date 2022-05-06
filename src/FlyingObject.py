from cmath import cos, sin
from SpaceObject import SpaceObject
from Velocity2d import Velocity2d

class FlyingObject(SpaceObject):

    def __init__(self, x, y, radius, mass, startSpeed, startHeading, imageLink):
        super().__init__(x, y, radius, mass, imageLink)
        self.startSpeed = startSpeed
        self.startHeading = startHeading
        
        xspeed = (startSpeed * cos(startHeading)).real
        yspeed = (startSpeed * sin(startHeading)).real
        self.velocity = Velocity2d(xspeed, yspeed)
        
    def update(self):
        self.x += self.velocity.x
        self.y -= self.velocity.y
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        print(str(self.rect.x) + ", " + str(self.rect.y))
        # self.rect.x += self.velocity.x
        # self.rect.y += self.velocity.y
        
    def distanceBetween(self, spaceObject):
        assert isinstance(spaceObject, SpaceObject)
        
    @staticmethod
    def determineVelocityVector(speed, heading):
        xspeed = speed * cos(heading)
        yspeed = speed * sin(heading)
        return Velocity2d(xspeed, yspeed)
        