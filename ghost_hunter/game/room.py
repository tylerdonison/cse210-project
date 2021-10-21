import arcade
from pytiled_parser.layer import Layer
from pytiled_parser.tiled_object import Polygon
from shapely.geometry import Polygon
from shapely.geometry import Point
from random import *
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Room():
    def __init__(self, layer):
        self.layer = layer
        self.polygon = Polygon
        self.points = []
        self.get_polygon()
    
    def get_polygon(self):
        points = []
        data = self.layer.data
       
        for i in range(1, len(data)-1):
           
            for j in range(1, len(data[i]) - 1):
                if data[i][j] != 0:
                    if data[i-1][j] == 0 or data[i-1][j-1] == 0 or data[i][j-1] == 0 or data[i+1][j] == 0 or data[i][j+1] == 0 or data[i+1][j+1] == 0:
                        #print(f"i: {i} j: {j} value: {data[i][j]}")
                        #print(f"x: {j*128 + 45} y: {1792 - (i-1) * 128 + 85}")
                        self.points.append(
                            Point(j*128 + 64, 1792 - (i-1) * 128 + 64))
        self.polygon = Polygon(self.points)

    def generate_random(self):
        minx, miny, maxx, maxy = self.polygon.bounds
        while True:
            pnt = Point(uniform(minx, maxx), uniform(miny, maxy))
            if self.polygon.contains(pnt):
                return pnt

