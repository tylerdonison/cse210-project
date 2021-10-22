""" Pause screen gives players options to pause the game,quit,exit the game, or get instructions."""
from PIL import Image
import arcade
import arcade.gui
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.image_loader import Image_Loader
from game.setup import setup
from game.instruction_screen import InstructionScreen
from ghost_hunter.game.title_screen import TitleScreen


class PauseScreen(arcade.View):
    """Code that runs at the start of the game or when the title screen is called.
    """

    def __init__(self):
        """Class Constructor
        """
        super().__init__()
        self.texture = arcade.load_texture(Image_Loader().get_pause_screen())

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        continue_button = arcade.gui.UIFlatButton(text="Continue", width=200)
        self.v_box.add(continue_button.with_space_around(bottom=20))

        instruction_button = arcade.gui.UIFlatButton(text="How to Play", width=200)
        self.v_box.add(instruction_button.with_space_around(bottom=20))

        exit_button = arcade.gui.UIFlatButton(text="Exit to Main Menu", width=200)
        self.v_box.add(exit_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Exit Program", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        continue_button.on_click = self.on_click_start
        instruction_button.on_click = self.on_click_instruction
        exit_button.on_click = self.on_click_exit
        quit_button.on_click = self.on_click_quit

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )        

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        self.manager.draw() 

    def on_click_start(self, event):
        """On click start event

        Args:
            event (Arcade.view): instance of PauseScreen ???
        """
        game_view = setup()
        game_view.setup()
        self.window.show_view(game_view)
    
    def on_click_instruction(self, event):
        """On click instructions event

        Args:
            event (arcade.view): On click instructions
        """
        game_view = InstructionScreen()
        game_view.on_draw()
        self.window.show_view(game_view)

    def on_click_exit(self, event):
        """On Click exit event

        Args:
            event (arcade.view): On Click exits
        """
        game_view = TitleScreen()
        game_view.on_draw()
        self.window.show_view(game_view)

    def on_click_quit(self, event):
        """On Click quit

        Args:
            event (arcade.view): On click quit the game
        """
        arcade.exit()
