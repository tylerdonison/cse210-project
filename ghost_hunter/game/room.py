"""Rooms include dinning, bedroom and bathroom. Generates a random room for the ghost.
"""
import arcade
from pytiled_parser.layer import Layer
from pytiled_parser.tiled_object import Polygon
from shapely.geometry import Polygon
from shapely.geometry import Point
from random import *
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Room():
    """Class Room generates the coordinates for the room which displays as Polygons and sets up layers for these rooms.
    """
    def __init__(self, layer):
        """Class Constructor

        Args:
            layer (self): creates room layers
        """
        self.layer = layer
        self.polygon = Polygon
        self.points = []
        self.get_polygon()
    
    def get_polygon(self):
        """gets the polygon dimensions
         Args:
             self: instance of Room
        """
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
        """Generates a random selection of room

        Returns:
            self: while in bounds returns pnt 
        """
        minx, miny, maxx, maxy = self.polygon.bounds
        while True:
            pnt = Point(uniform(minx, maxx), uniform(miny, maxy))
            if self.polygon.contains(pnt):
                return pnt

