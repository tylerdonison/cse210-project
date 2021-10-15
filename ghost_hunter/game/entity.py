"""The class in charge of holding information about the entities in the game."""

import arcade
from game.constants import CHARACTER_SCALING

class Entity:
  """The Entity class helps store common information about the entities in the game.

  Stereotype: Information Holder

  Attributes:
    sprite(SpriteList): The SpriteList that contains the entity.
  """
  def __init__(self):
    """The class constructor

    Args:
    self (Entity): An instance of Entity
    """
    self.sprite = arcade.SpriteList()
  
  def setup(self, resource, x, y):
      """This sets up the entity by setting it's image source and position.

      Args:
        self (Entity): An instance of Entity
        resources (string): the image source of the sprite
        x (int): the x coordinate of the center of the sprite
        y (int): the y coordinate of the center of the sprite
      """
      image_source = resource
      self.sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
      self.sprite.center_x = x
      self.sprite.center_y = y
