from cmath import cos, sin, sqrt
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
        self.y += self.velocity.y
        
        self.rect.x = self.x
        self.rect.y = self.y
        
    def setSpeedAndHeading(self, speed, heading):
        xspeed = (speed * cos(heading)).real
        yspeed = (speed * sin(heading)).real
        self.velocity = Velocity2d(xspeed, yspeed)

    @staticmethod
    def determineVelocityVector(speed, heading):
        xspeed = (speed * cos(heading)).real
        yspeed = (speed * sin(heading)).real
        return Velocity2d(xspeed, yspeed)
        