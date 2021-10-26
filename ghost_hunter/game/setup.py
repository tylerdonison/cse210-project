"""The main class of the game used to control all the other classes."""

import arcade
from arcade import camera
from arcade import sprite_list
from arcade.sprite import Sprite
from game.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH 
from game.constants import CHARACTER_SCALING, TILE_SCALING
from game.constants import PLAYER_MOVEMENT_SPEED, PLAYER_START_X, PLAYER_START_Y
from game.constants import ROOM_LIST, INSTRUMENTS, GHOST_TYPES
from game import images
from game.player import Player
from arcade.experimental.lights import Light, LightLayer
from game.ghost import Ghost
from game.image_loader import Image_Loader
from game.sound_loader import Sound_Loader
from game.victory import VictoryScreen
from game.game_over import GameOverScreen
from game.room import Room
from game.handle_collisions_action import Handle_Collisions_Action
from random import randint
import sys
from threading import Timer
from game import constants

AMBIENT_COLOR = (10, 10, 10)

class setup(arcade.View):
    """Main application class.

    Stereotype: Controller

    Args:
        _tile_map(TileMap): the map with all the tiles
        _scene(Scene): the scene of the game
        _player(Player): the player of the game
        _physics_engine(PhysicsEngineSimple): the physics engine of the game
        _camera(Camera): a camera to use for scrolling
        _gui_camera(Camera): a gui camera
        _player_light(Layer): a layer for the player light
        _light_layer(Layer): a layer for the light
        _room_map(Room): a room instance for the room the ghost is in
        _instruments(Array): the instruments the player can use
        _handle_collisions_action(Handle_Collision_Action): an instance of Handle_Collision_Action to use for collisions
        _room_name(string): the name of the room the ghost starts in
        _ghost(Ghost): the ghost from the game
        _sound_loader(Sound_Loader): an instance of Sound_Loader
        _emf(int): the emf value
        _red_timer(int): the red timer
        _white_timer (int): the white timer
    """

    def __init__(self):
        """The Class Constructor

        Args:
            self(setup): an instance of setup
        """
        # Call the parent class and set up the window
        super().__init__()
        
        # TileMap Object
        self._tile_map = None

        # Our Scene Object
        self._scene = None
        
        # Separate variable that holds the player sprite
        self._player = Player()
        self._player.center_x = PLAYER_START_X
        self._player.center_y = PLAYER_START_Y

        # Our physics engine
        self._physics_engine = None

        # A Camera that can be used for scrolling the screen
        self._camera = None

        # A Camera that can be used to draw GUI elements
        self._gui_camera = None

        #Layers that will cover the tiled map
        self._player_light = None
        self._light_layer = None
        
        self._room_map = None
        self._instruments = []


        self._handle_collisions_action = None

        self._room_name = ROOM_LIST[randint(0, len(ROOM_LIST) - 1)]

        self._ghost = None

        arcade.set_background_color(arcade.csscolor.BLACK)
        
        #Load sound loader
        self._sound_loader = Sound_Loader()

        self._emf = 1
        self._red_timer = 0
        self._white_timer = 0
        self.heart_beat = None

    def setup(self):
        """Set up the game here. Call this function to restart the game.
        
        Args:

            self(setup): an instance of setup
            self: map
            self: Ghost Sprite
            self: Player
            self: camera
            self: physics engine
            self: light layer
         """

        self.setup_camera()

        self.draw_map()  
        self._ghost = Ghost(self._player, self._room_map, self._instruments[3])
        self.player_setup()
        # Create the 'physics engine'
        self._physics_engine = arcade.PhysicsEngineSimple(
            self._player.sprite, self._scene.get_sprite_list("Walls"))
    
        self._light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self._light_layer.set_background_color(arcade.color.BLACK)
        self._player_light = Light(0, 0, 180,  arcade.csscolor.WHITE, 'soft')
        
        self.red_light_layer = Light(0, 0, 180, arcade.csscolor.BLACK, 'soft')
        
    def setup_camera(self):
        """Setup the Cameras
        
        Args:
            self(setup): an instance of setup
        """
        self._camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self._gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    def setup_instruments(self):
        """
        Sets up the instruments that are used to capture the ghost

        Args:
            self(setup): an instance of setup
        """        
        instrument = arcade.Sprite(
                Image_Loader().get_thermos(), CHARACTER_SCALING / 16)
        instrument.set_position(750, 160)
        self._instruments.append(instrument)
        self._scene.add_sprite(INSTRUMENTS[0], self._instruments[0])
        instrument = arcade.Sprite(
            Image_Loader().get_vacuum(), CHARACTER_SCALING / 8)
        instrument.set_position(830, 160) 
        self._instruments.append(instrument)
        self._scene.add_sprite(INSTRUMENTS[1], self._instruments[1])
        instrument = arcade.Sprite(
            Image_Loader().get_bible(), CHARACTER_SCALING / 60)
        instrument.set_position(910, 160) 
        self._instruments.append(instrument)
        self._scene.add_sprite(INSTRUMENTS[2], self._instruments[2])
        instrument = arcade.Sprite(
            Image_Loader().open_book, CHARACTER_SCALING / 4.5)
        instrument.set_position(990, 160)
        self._instruments.append(instrument)
        self._scene.add_sprite(INSTRUMENTS[3], self._instruments[3])   
        
    def draw_map(self):
        """This function draws the map using the image loader

        Args:
            self(setup): an instance of setup
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
        self._tile_map = arcade.load_tilemap(
            map_name, TILE_SCALING, layer_options)
        self._scene = arcade.Scene.from_tilemap(self._tile_map)
        room_layer = self._tile_map.get_tilemap_layer(self._room_name)
        self._room_map = Room(room_layer, self._room_name)
        if self._tile_map.tiled_map.background_color:
            arcade.set_background_color(self._tile_map.tiled_map.background_color)

        self.setup_instruments()
    
    def player_setup(self):
        """ This function sets up the player and ghost sprites.

        Args:
            self(setup): an instance of setup
        """
        self._scene.add_sprite("Player", self._player.sprite)
        self._player._set_center_x(PLAYER_START_X)
        self._player._set_center_y(PLAYER_START_Y)
        self._scene.add_sprite("Ghost", self._ghost.sprite)

    def on_draw(self):
        """Render the screen.
        
        Args:
            self(setup): an instance of setup

            """
        # Clear the screen to the background color
        arcade.start_render()

        # Activate the game camera
        self._camera.use()

        # Draw our Scene with the light_layer
        with self._light_layer:
            self._scene.draw()
        
        self._light_layer.draw(ambient_color=AMBIENT_COLOR)
        self._light_layer.add(self._player_light)

        # Activate the GUI camera before drawing GUI elements
        self._gui_camera.use()

        #draw the sanity box
        sanity_text = f"Sanity: {self._player.sanity}%"
        arcade.draw_text(sanity_text, 10, 10, arcade.csscolor.WHITE, 18,)

        emf_text = f"Emf: {self._emf}"
        arcade.draw_text(emf_text, SCREEN_WIDTH - 110,  10, arcade.csscolor.WHITE, 18,)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed.
        
        Args:
            self(setup): an instance of setup
            key(Key): the key that was pressed
        """
        if key == arcade.key.UP or key == arcade.key.W:
            self._sound_loader.play_single_footstep_sound()
            self._player.character_direction = 0
            self._player.sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self._sound_loader.play_single_footstep_sound()
            self._player.character_direction = 1
            self._player.sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self._sound_loader.play_single_footstep_sound()
            self._player.character_direction = 3
            self._player.sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self._sound_loader.play_single_footstep_sound()
            self._player.character_direction = 2
            self._player.sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            #could pick or leave 
            if self._player.has_instrument:
                self._player.has_instrument = False
                self._player.index_of_instrument = None
            else:
                self.collision_with_instruments()
        elif key == arcade.key.ESCAPE:
            game_view = GameOverScreen(self._ghost.ghost_type)
            game_view.on_draw()
            self.window.show_view(game_view)
                
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key.        
        Args:
            self(setup): an instance of setup
            key(Key): the key that was pressed
        """
        if key == arcade.key.UP or key == arcade.key.W:
            self._player.sprite.change_y = 0
            #player animation
            self._sound_loader.play_single_footstep_sound()
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self._player.sprite.change_y = 0
            #player animation
            self._sound_loader.play_single_footstep_sound()
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self._player.sprite.change_x = 0
            #player animation
            self._sound_loader.play_single_footstep_sound()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self._player.sprite.change_x = 0
            #player animation
        else:
            self._player.sprite.change_x = 0
            self._sound_loader.play_single_footstep_sound()


    def center_camera_to_player(self):
        """This function centers the camera on the player.

        Args:
            self(setup): an instance of setup
        """
        screen_center_x = self._player.sprite.center_x - (self._camera.viewport_width / 2)
        screen_center_y = self._player.sprite.center_y - (
            self._camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self._camera.move_to(player_centered)
    
    def on_update(self, delta_time):
        """Updates the screen with players new position and the light position.
        
        Args:

            self(setup): an instance of setup
            delta_time(int): the delta time for the update
        """
        self._physics_engine.update()
        self._player_light.position = self._player.sprite.position
        if self._player.has_instrument:
            new_position = self._player.sprite.position

            index_of_instrument = self._player.index_of_instrument
            self._instruments[index_of_instrument].center_x = self._player.sprite.center_x + 35
            self._instruments[index_of_instrument].center_y = self._player.sprite.center_y - 50

        self.center_camera_to_player()

        self._emf = self._ghost.execute(self._player.sanity, self._scene, self._scene.get_sprite_list("Walls"), self._room_map, self._instruments)

        #light change for hunting mode on
        if self._ghost.hunt_mode_on:
            if self._player_light._color == arcade.csscolor.WHITE:
                self._red_timer += 1
                if self._red_timer % 30 == 0:
                    if randint(0,2):
                        self._player_light._color = arcade.csscolor.BLACK
            else:
                if randint(0, 2):
                    self._player_light._color = arcade.csscolor.WHITE
        elif self._player_light._color == arcade.csscolor.BLACK:
            self._white_timer += 1
            if self._white_timer % 120 == 0:
                self._player_light._color = arcade.csscolor.WHITE
        
        self.collision_with_ghost()
        self.heart_beat = self._ghost.heart_beat

    def collision_with_instruments(self):

        """Handles the collision with instruments

        Args:
            self(setup): an instance of setup 
        """

        self._handle_collisions_action = Handle_Collisions_Action(
            self._player, self._ghost, self._instruments)
        if self.handle_collisions_action.check_collision_between_player_and_ghost():
            if self._ghost.check_correct_instrument(self._player.index_of_instrument):
                arcade.stop_sound(self.heart_beat)
                self.game_end(self._ghost.ghost_type)
            else:
                arcade.stop_sound(self.heart_beat)
                self.game_over(self._ghost.ghost_type)
                
        index_of_instrument = self._handle_collisions_action.check_collision_between_player_and_instruments() 
        if index_of_instrument != None and index_of_instrument != self._player.index_of_instrument:
            self._player.set_instrument(index_of_instrument)
            self._instruments[index_of_instrument].center_x = self._player.sprite.center_x + 35
            self._instruments[index_of_instrument].center_y = self._player.sprite.center_y - 50
            self._handle_collisions_action.instrument_to_ignore = index_of_instrument

    def collision_with_ghost(self):
        """Handles the collision with the ghost

        Args:
            self(setup): an instance of setup
        """
 
        self.handle_collisions_action = Handle_Collisions_Action(
            self._player, self._ghost, self._instruments)
        if self.handle_collisions_action.check_collision_between_player_and_ghost():
            if self._player.index_of_instrument == None:
                self.game_over(self._ghost.ghost_type)
                arcade.stop_sound(self.heart_beat)

            elif self.check_if_correct_instrument():
                self.game_end(self._ghost.ghost_type)
                arcade.stop_sound(self.heart_beat)

            else:
                self.game_over(self._ghost.ghost_type)
                arcade.stop_sound(self.heart_beat)

    def check_if_correct_instrument(self):
        """Checks if the player has the correct instrument to catch the ghost

        Args:
            self(setup): an instance of setup
        """
        if constants.INSTRUMENTS[self._player.index_of_instrument] == constants.INTRUMENT_NEEDED[self._ghost.ghost_type]:
            return True
        return False

    def game_over(self, ghost_type = "Penguin"):
        """The game is over
        Args:
            self(setup): an instance of setup
        """
        game_over_screen = GameOverScreen(ghost_type)
        self.window.show_view(game_over_screen)
    
    def game_end(self, ghost_type = "Penguin"):
        """The game has ended because the ghost was caught.

        Args:
            self(setup): an instance of setup
        """
        victory_screen = VictoryScreen(ghost_type)
        self.window.show_view(victory_screen)
