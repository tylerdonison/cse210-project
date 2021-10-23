"""This file keeps track of the constants for the game, such as the rooms, speed of Sprites, 
coordinates of furniture, demensions of the rooms, screen size, title, instruments used to capture the ghost,
for the area of play.

"""
import os

ROOM_LIST = ["Dinning Room", "Bedroom", "Bathroom"]
INTERACTIONS_DICTIONARY = { "Dinning Room":["Sink","Television","Couch"], 
                            "Bedroom":["Bed","Computer","Dresser"], 
                            "Bathroom":["Sink","Bathtub","Toilet"]}
                            
OBJECT_COORDINATES = {"Sink":[196,800], "Television":[384,600], "Couch":[700,1400], "Bed":[896,1500], 
"Computer":[1280,1400], "Dresser":[1280,1000], "Sink":[896,576], "Bathtub":[1280,576], "Toilet":[1280,900]}

INSTRUMENTS = ["Vacuum", "Ghost Thermo", "Bible", "Journal"]
#ROOM MAX COORDINATES = [MIN X, MIN Y, MAX X, MAX Y]
DINNING_MAX_COORDINATES = [192, 576, 704, 1600]
BEDROOM_MAX_COORDINATES = [960, 1088, 1472, 1600]
BATHROOM_MAX_COORDINATES = [960, 576, 1472, 832]
TOTAL_MAX_COORDINATES = [192, 575, 1472, 1600]
COORINATE_DICTIONARY = {"Dinning Room": [192, 576, 704, 1600], "Bedroom": [960, 1088, 1472, 1600], "Bathroom": [960, 576, 1472, 832]}

GHOST_TYPES = ["poltergeist", "wraith", "demon"]

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Python Ghost Hunter"

INTERVAL_BEFORE_HUNT = 4
TILE_SCALING = 1
CHARACTER_SCALING = 1
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING
PLAYER_MOVEMENT_SPEED = 5
GHOST_MOVEMENT_SPEED = 1
HUNT_DURATION = 1 #15
MAX_COOLDOWN_TIME = 15
TIME_BETWEEN_PROBABILITES = 1 #10 #number of seconds between when the "dice" are rolled for a ghost action

LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 100

PLAYER_START_X = 550
PLAYER_START_Y = 200
