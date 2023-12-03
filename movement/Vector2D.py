from math import atan2
from math import cos, sin, radians

class Vector2D:
    def __init__(self, angle, length):
        self._length = length
        self._angle = angle
        self._x = length * cos(radians(angle))
        self._y = length * sin(radians(angle))

    def getComponents(self):
        return [self._x, self._y]

    def abs(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def cdot(self, param):
        if isinstance(param, Vector2D):
            p_x, p_y = param.getComponents()
            return self._x * p_x + self._y * p_y
        else:
            raise ValueError("Parameter must be an instance of Vector2D")

    def getAngle(self):
        return atan2(self._y, self._x)
