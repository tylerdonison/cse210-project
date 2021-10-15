"""This is the module in charge of controlling the ghost
"""
import arcade
from game.ghost_mode_action import Action_Mode
from game.ghost_mode_hunt import Hunt_Mode
import os
from game.constants import CHARACTER_SCALING
from game.entity import Entity

class Ghost(Entity):
    """The ghost is a spooky being who leaves clues and hunts the player.

    Stereotype: Information Holder, Controller

    Attributes:
        cooldown_time (int): The cooldown time for hunt mode.
        hunt_time (int): The duration of the hunt.
        time_since_last_interaction (int): The time that passed since the last interaction.
        hunt_mode_on (boolean): Whether the ghost is hunting or not.
        hunt_mode (Hunt_Mode): A Hunt_Mode object to control the hunt mode of the ghost.
        action_mode (Action_Mode): A Action_Mode object to control the action mode of the ghost.
        hunt_duration (int): The duration of a hunt
        max_cooldown_time (int): The maximum a cooldown can last. 
    """
    def __init__(self):
        """The class constructor

        Args:
            self (Ghost): An instance of Ghost
        """
        Entity.__init__(self)
        path = r'C:\CSE210\cse210-project\ghost_hunter\game\images'
        self.sprite = arcade.Sprite(os.path.join(
            path, "ghost_front_sprite.png"), CHARACTER_SCALING)
        #need to change its position to be a random one inside one of the rooms
        Entity.setup(
            self,  os.path.join(
                path, "ghost_front_sprite.png"), 500, 500)
        
        self.cooldown_time = 0
        self.hunt_time = 0
        self.time_since_last_interaction = 0
        self.hunt_mode_on = False
        self.hunt_mode = Hunt_Mode()
        self.action_mode = Action_Mode()
        self.hunt_duration = 15
        self.max_cooldown_time = 30


    def execute(self,sanity):
        """This executes all of the updates and actions that the ghost object should have during
        each cycle.

        Args: 
            self (Ghost): An instance of Ghost
            sanity (int): the players current sanity
        """
        self.update_time_and_status(sanity)
        self.do_interaction()
        self.do_hunt()

    def update_time_and_status(self,sanity):
        """This method updates the cooldown time or, if the ghost is hunging, the hunt time.

        Args: 
            self (Ghost): An instance of Ghost
            sanity (int): the players current sanity
        """
        if self.hunt_mode_on == True:
            self.hunt_time += 1
            self.cooldown_time = 0
        else:
            self.cooldown_time +=1
            self.time_since_last_interaction += 1


        if self.cooldown_time > self.max_cooldown_time:
            self.hunt_mode_on = self.hunt_mode.hunt_check(sanity)
            self.cooldown_time -= 5 #this prevents the hunt mode from checking every second after cooldown time is greater than 30

        if self.hunt_time > self.hunt_duration:
            self.hunt_mode_on == False
            self.hunt_time = 0

    def do_interaction(self):
        """This method first checks to see if the ghost is hunting. If it is not, it calls the cause_ghost_interaction
        method.

        Args:
            self (Ghost): An instance of Ghost
        """    
        if (self.hunt_mode_on == False) and (self.time_since_last_interaction > 45):
            self.action_mode.cause_ghost_interaction()
            self.time_since_last_interaction = 0

    def do_hunt(self):
        """If hunt_mode is active, this will cause the ghost to hunt the player.

        Args:
            self (Ghost): An instance of Ghost
        """
        if self.hunt_mode_on == True:
            self.hunt_mode.hunt()

    def move_ghost(self):
        pass
