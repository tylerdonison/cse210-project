import arcade
from game.setup import setup

def main():
    """Main function"""
    window = setup()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()