import arcade
from arcade import camera
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH 
from game.constants import CHARACTER_SCALING, TILE_SCALING
from game.constants import PLAYER_MOVEMENT_SPEED, PLAYER_START_X, PLAYER_START_Y
from game import images
from game.player import Player
from arcade.experimental.lights import Light, LightLayer
from game.ghost import Ghost
from game.image_loader import Image_Loader

AMBIENT_COLOR = (10, 10, 10)

class setup(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None
        
        # Separate variable that holds the player sprite
        self.player = Player()

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        #Layers that will cover the tiled map
        self.player_light = None
        self.light_layer = None

        self.clock = 0
        self.ghost = Ghost()


        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.setup_camera()
        self.draw_map()   
        self.player_setup()
        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player.sprite, self.scene.get_sprite_list("Walls))
        
        
        self.light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)
        self.player_light = Light(0, 0, 150,  arcade.csscolor.WHITE, 'soft')


    def setup_camera(self):
        """Setup the Cameras"""
        
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

    def draw_map(self):
        map_name = Image_Loader().get_map_name()
        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.        
        layer_options = {
            "Walls": {
                "use_spatial_hash": True,
            },
            # "Room Names":{
            #     "use_spatial_hash": True,
            # },
        }        
        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(
            map_name, TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        # Set the background color
        if self.tile_map.tiled_map.background_color:
            arcade.set_background_color(self.tile_map.tiled_map.background_color)
    
    def player_setup(self):
        self.scene.add_sprite("Player", self.player.sprite)
        self.scene.add_sprite("Ghost", self.ghost.sprite)

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        arcade.start_render()

        # Activate the game camera
        self.camera.use()

        # Draw our Scene with the light_layer
        with self.light_layer:
            self.scene.draw()
        
        self.light_layer.draw(ambient_color=AMBIENT_COLOR)
        self.light_layer.add(self.player_light)

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player.sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)
    
    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player_light.position = self.player.sprite.position
        self.center_camera_to_player()
        self.ghost.execute(self.player.sanity)
        
