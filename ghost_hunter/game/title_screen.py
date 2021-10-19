from PIL import Image
import arcade
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.image_loader import Image_Loader
from game.setup import setup


class TitleScreen(arcade.View):
    """Code that runs at the start of the game or when the title screen is called.
    """

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(Image_Loader().get_title_screen())

        # Reset the viewport
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = setup()
        game_view.setup()
        self.window.show_view(game_view)