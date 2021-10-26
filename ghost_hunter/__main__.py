"""Main function in the game"""
import arcade
from game.setup import setup
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH
from game.menu_director import MenuDirector
import sys

def main():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MenuDirector()
    window.show_view(start_view)
    arcade.run()
    thunder = start_view.thunder
    arcade.sound.stop_sound(thunder)
    arcade.exit
    sys.exit

if __name__ == "__main__":
    main()
