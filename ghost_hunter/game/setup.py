import arcade
from arcade import camera
from arcade import sprite_list
from arcade.sprite import Sprite
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH 
from game.constants import CHARACTER_SCALING, TILE_SCALING
from game.constants import PLAYER_MOVEMENT_SPEED, PLAYER_START_X, PLAYER_START_Y
from game.constants import ROOM_LIST, INSTRUMENTS
from game import images
from game.player import Player
from arcade.experimental.lights import Light, LightLayer
from game.ghost import Ghost
from game.image_loader import Image_Loader
from game.sound_loader import Sound_Loader
from game.room import Room
from game.handle_collisions_action import Handle_Collisions_Action
from random import randint
import sys
from threading import Timer

AMBIENT_COLOR = (10, 10, 10)

class setup(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """The Class Constructor
        """
        # Call the parent class and set up the window
        super().__init__()
        
        # TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None
        
        # Separate variable that holds the player sprite
        self.player = Player()
        self.player.center_x = PLAYER_START_X
        self.player.center_y = PLAYER_START_Y

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        #Layers that will cover the tiled map
        self.player_light = None
        self.light_layer = None
        self.red_light_layer = None

        self.clock = 0
        
        self.room_map = None
        self.instruments = []

        self.handle_collisions_action = None

        self.room_name = ROOM_LIST[randint(0, len(ROOM_LIST) - 1)]

        self.ghost = None
        print(self.room_name)

        arcade.set_background_color(arcade.csscolor.BLACK)
        
        #Load sound loader
        self.sound_loader = Sound_Loader()

        self.emf = 1
        self.red_timer = 0
        self.white_timer = 0

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.setup_camera()
        #Need to pick ghost room before draw_map
        self.draw_map()  
        self.ghost = Ghost(self.player, self.room_name, self.instruments[3])
        self.player_setup()
        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player.sprite, self.scene.get_sprite_list("Walls"))
    
        
        self.light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)
        self.player_light = Light(0, 0, 150,  arcade.csscolor.WHITE, 'soft')

        self.red_light_layer = Light(0, 0, 150, arcade.csscolor.RED, 'soft')
        
        #choose random ghost type
        #choose random ghost location
        #call ghost to begin random actions, pass in player

    def setup_camera(self):
        """Setup the Cameras"""
        
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    def setup_instruments(self):
        """
        Sets up the instruments that are used to capture the ghost
        """
        instrument = arcade.Sprite(
                ":resources:images/topdown_tanks/tankRed_barrel3.png", CHARACTER_SCALING)
        instrument.set_position(800, 160)
        self.instruments.append(instrument)
        self.scene.add_sprite(INSTRUMENTS[0], self.instruments[0])
        instrument = arcade.Sprite(
            ":resources:images/topdown_tanks/tankGreen_barrel1.png", CHARACTER_SCALING)
        instrument.set_position(860, 160) 
        self.instruments.append(instrument)
        self.scene.add_sprite(INSTRUMENTS[1], self.instruments[1])
        instrument = arcade.Sprite(
            ":resources:images/topdown_tanks/tankDark_barrel3_outline.png", CHARACTER_SCALING)
        instrument.set_position(920, 160) 
        self.instruments.append(instrument)
        self.scene.add_sprite(INSTRUMENTS[2], self.instruments[2])
        instrument = arcade.Sprite(
            Image_Loader().open_book, CHARACTER_SCALING / 4.5)
        instrument.set_position(980, 160)
        self.instruments.append(instrument)
        self.scene.add_sprite(INSTRUMENTS[3], self.instruments[3])
        
        

    def draw_map(self):
        """This function draws the map using the image loader
        """
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
        room_layer = self.tile_map.get_tilemap_layer(self.room_name)

        try:
            self.room_map = Room(room_layer)
        except AttributeError:
            print("start error swept under the rug")
        if self.tile_map.tiled_map.background_color:
            arcade.set_background_color(self.tile_map.tiled_map.background_color)

        self.setup_instruments()
    
    def player_setup(self):
        """ This function sets up the player and ghost sprites
        """
        self.scene.add_sprite("Player", self.player.sprite)
        self.player._set_center_x(PLAYER_START_X)
        self.player._set_center_y(PLAYER_START_Y)
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

        #draw the sanity box
        sanity_text = f"Sanity: {self.player.sanity}%"
        arcade.draw_text(sanity_text, 10, 10, arcade.csscolor.WHITE, 18,)

        emf_text = f"Emf: {self.emf}"
        arcade.draw_text(emf_text, SCREEN_WIDTH - 110,  10, arcade.csscolor.WHITE, 18,)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.sound_loader.play_single_footstep_sound()
            self.player.character_direction = 0
            self.player.sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.sound_loader.play_single_footstep_sound()
            self.player.character_direction = 1
            self.player.sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.sound_loader.play_single_footstep_sound()
            self.player.character_direction = 3
            self.player.sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.sound_loader.play_single_footstep_sound()
            self.player.character_direction = 2
            self.player.sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            #could pick or leave 
            if self.player.has_instrument:
                self.player.has_instrument = False
                self.player.index_of_instrument = None
            else:
                self.collision_with_instruments()
                
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.sprite.change_y = 0
            #player animation
            self.sound_loader.play_single_footstep_sound()
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.sprite.change_y = 0
            #player animation
            self.sound_loader.play_single_footstep_sound()
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.sprite.change_x = 0
            #player animation
            self.sound_loader.play_single_footstep_sound()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.sprite.change_x = 0
            #player animation
        else:
            self.player.sprite.change_x = 0
            self.sound_loader.play_single_footstep_sound()


    def center_camera_to_player(self):
        """This function centers the camera on the player
        """
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
        """Updates the screen with players new position and the light position."""
        self.physics_engine.update()
        self.player_light.position = self.player.sprite.position
        if self.player.has_instrument:
            new_position = self.player.sprite.position

            index_of_instrument = self.player.index_of_instrument
            self.instruments[index_of_instrument].center_x = self.player.sprite.center_x + 35
            self.instruments[index_of_instrument].center_y = self.player.sprite.center_y - 50
        self.center_camera_to_player()

        self.emf = self.ghost.execute(self.player.sanity, self.scene, self.scene.get_sprite_list("Walls"), self.room_map, self.instruments)

        #light change for hunting mode on
        if self.ghost.hunt_mode_on:
            if self.player_light._color == arcade.csscolor.WHITE:
                self.red_timer += 1
                if self.red_timer % 30 == 0:
                    if randint(0,2):
                        self.player_light._color = arcade.csscolor.BLACK
                        

            else:
                if randint(0, 2):
                    self.player_light._color = arcade.csscolor.WHITE
        elif self.player_light._color == arcade.csscolor.BLACK:
            self.white_timer += 1
            if self.white_timer % 120 == 0:
                self.player_light._color = arcade.csscolor.WHITE
        
        self.collision_with_ghost()

    """capture ghost via the room, not the physical ghost's presence"""
    def collision_with_instruments(self):

        """Handles capturing the ghost and updates the collisions 
        """
        self.handle_collisions_action = Handle_Collisions_Action(
            self.player, self.ghost, self.instruments)


        index_of_instrument = self.handle_collisions_action.check_collision_between_player_and_instruments() 
        if index_of_instrument != None and index_of_instrument != self.player.index_of_instrument:
            self.player.set_instrument(self.instruments[index_of_instrument], index_of_instrument)
            self.instruments[index_of_instrument].center_x = self.player.sprite.center_x + 35
            self.instruments[index_of_instrument].center_y = self.player.sprite.center_y - 50
            self.handle_collisions_action.instrument_to_ignore = index_of_instrument


    def collision_with_ghost(self):
        self.handle_collisions_action = Handle_Collisions_Action(
            self.player, self.ghost, self.instruments)
        if self.handle_collisions_action.check_collision_between_player_and_ghost():
            if self.ghost.check_correct_instrument(self.player.index_of_instrument):
                self.game_end()
            else:
                #self.game_over()
                sys.exit


    def game_over(self):
        """The game is over"""
        self.window.close()
    
    def game_end(self):
        """The game has ended because the ghost was caught. w
        """
        self.window.close()
