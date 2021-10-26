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

    Args:
        layer(MapLayer): the layer that contains the room.
        polygon(Polygon): the polygon that contains the room.
        name(string): the name of the room
    """

    def __init__(self, layer, name):
        """Class Constructor

        Args:
            self (Room): an instance of Room
            layer (Layer): a layer for the room
            name (string): the name of the room
        """
        self.layer = layer
        self.name = name
        self.polygon = Polygon
        self.get_polygon()

    def get_polygon(self):
        """Gets the polygon dimensions of the room

         Args:
             self: instance of Room
        """
        if not self.layer:
            return
        points = []
        data = self.layer.data

        for i in range(1, len(data)-1):

            for j in range(1, len(data[i]) - 1):
                if data[i][j] != 0:
                    if data[i-1][j] == 0 or data[i-1][j-1] == 0 or data[i][j-1] == 0 or data[i+1][j] == 0 or data[i][j+1] == 0 or data[i+1][j+1] == 0:
                        points.append(
                            Point(j*128 + 64, 1792 - (i-1) * 128 + 64))
        self.polygon = Polygon(points)

    def generate_random(self):
        """Generates a random selection from room

        Args:
            self(Room): a Room instance

        Returns:
            Point: a random point inside the room
        """
        minx, miny, maxx, maxy = self.polygon.bounds
        while True:
            pnt = Point(uniform(minx, maxx), uniform(miny, maxy))
            if self.polygon.contains(pnt):
                return pnt
