import arcade
from game.setup import setup
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH
from game.title_screen import TitleScreen

def main():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = TitleScreen()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()