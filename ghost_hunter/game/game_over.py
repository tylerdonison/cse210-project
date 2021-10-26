"""The Game Over screen is shown when the player is defeated by the ghost. The
type of ghost is displayed and the player can close the game.
"""
from PIL import Image
import arcade
import arcade.gui
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.image_loader import Image_Loader
from game.ghost import Ghost

class GameOverScreen(arcade.View):
    """Code that runs when the player is defeated by the ghost.
    """

    def __init__(self, ghost_type):
        """Class Constructor

        Args:
            self: An instance of the GameOverScreen class
            ghost_type: the ghost type that the player was defeated by
        """
        super().__init__()
        self.ghost_type = ghost_type

        if self.ghost_type == "demon":
            self.texture = arcade.load_texture(Image_Loader().get_demon_game_over_screen())
        elif self.ghost_type == "wraith":
            self.texture = arcade.load_texture(Image_Loader().get_wraith_game_over_screen())
        elif self.ghost_type == "poltergeist":
            self.texture = arcade.load_texture(Image_Loader().get_poltergeist_game_over_screen())
        
    def on_draw(self):
        """ Draw this view

        Args:
            self: an instance of the GameOverScreen class
        """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_key_press(self, key, modifiers):
        """Called when a key is pressed.

        Args:
            self: an instance of the GameOverScreen class
            key: an Arcade parameter that identifies when the player presses a key
        """
        if key == arcade.key.ENTER:
            self.window.close()
            arcade.exit()
