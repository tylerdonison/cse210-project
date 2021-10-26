"""menu director for the screen that starts the game allows visitors
"""
import arcade
import arcade.gui
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.image_loader import Image_Loader
from game.sound_loader import Sound_Loader
from game.setup import setup


class MenuDirector(arcade.View):
    """MenuDirector class is a of arcade view superclass. 

    Args:
        arcade (superclass): viewport window
    """
    def __init__(self):
        """The class constructor
        """
        super().__init__()
        self.texture = arcade.load_texture(Image_Loader().get_title_screen())

        # Reset the viewport
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box1 = arcade.gui.UIBoxLayout()
        self.v_box2 = arcade.gui.UIBoxLayout()
        self.v_box3 = arcade.gui.UIBoxLayout()
        
        # Load Sound
        self.sound_loader = Sound_Loader()

        self.thunder = "pie"

        # Create the buttons
        self.button1 = arcade.gui.UIFlatButton(text="How to Play", width=200)
        self.v_box1.add(self.button1.with_space_around(bottom=20))

        self.button2 = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box2.add(self.button2.with_space_around(bottom=20))

        self.button3 = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box3.add(self.button3.with_space_around(bottom=20))
        
        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        self.button1.on_click = self.on_click_button1
        self.button2.on_click = self.on_click_button2
        self.button3.on_click = self.on_click_button3

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="bottom",
                child=self.v_box1)
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="bottom",
                child=self.v_box2)
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.v_box3)
        )

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        self.manager.draw() 

    def on_click_button1(self, event):
        """on click button event show how to play the game

        Args:
            event (arcade): instance of Arcade view
        """
        if self.button1._text == "How to Play":
            self.texture = arcade.load_texture(Image_Loader().get_instruction_screen())
            self.button1._text = "Ghost Types"
            self.on_draw()
            self.window.show_view(self)
        elif self.button1._text == "Ghost Types":
            self.texture = arcade.load_texture(Image_Loader().get_ghost_types_screen())
            self.button1._text = "How to Play"
            self.on_draw()
            self.window.show_view(self)

    def on_click_button2(self, event):
        """on click button event  Starts the game

        Args:
            event (arcade): instance of Director
        """
        game_view = setup()
        game_view.setup()
        self.window.show_view(game_view)
        self.sound_loader.play_evil_laugh()
        self.sound_loader.play_creaking_door()
        self.thunder = self.sound_loader.play_thunder()

    def on_click_button3(self, event):
        """On click event button 3 ends the game

        Args:
            event (arcade): exists the game
        """
        arcade.exit()
