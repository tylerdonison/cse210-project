import arcade
from game.constants import CHARACTER_SCALING
from game.constants import PLAYER_MOVEMENT_SPEED, PLAYER_START_X, PLAYER_START_Y
from game.constants import LIGHT_RADIUS

class Player:
    
    def __init__(self):
        self.sprite = arcade.SpriteList()
        self.player_setup()

    
    def player_setup(self):
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.sprite.center_x = PLAYER_START_X
        self.sprite.center_y = PLAYER_START_Y

