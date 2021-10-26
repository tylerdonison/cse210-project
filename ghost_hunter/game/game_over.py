"""The Game Over screen is shown when the player is defeated by the ghost. The
type of ghost is displayed and the player can close the game.
"""
from PIL import Image
import arcade
import arcade.gui
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.image_loader import Image_Loader
from game.ghost import Ghost

class GameOverScreen(arcade.Window):
    """Code that runs when the player is defeated by the ghost.
    """

    def __init__(self):
        """Class Constructor
        """
        super().__init__()
        self.texture = arcade.load_texture(Image_Loader().get_game_over_screen())
        
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text(f"{Ghost().ghost_type()}", start_x=700, start_y=350, Color=arcade.color.BOSTON_UNIVERSITY_RED, font_name="Garamond", align="center")

    def on_key_press(self, key, modifiers):
        """Called when a key is pressed.
        """
        if key == arcade.key.ENTER:
            self.window.close()
