import math


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, n, angle):
    arc_legth = 2 * math.pi