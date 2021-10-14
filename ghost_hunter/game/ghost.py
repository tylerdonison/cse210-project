"""This is the module in charge of controlling the ghost
"""
import arcade
from ghost_mode_action import Action_Mode
from ghost_mode_hunt import Hunt_Mode

class Ghost():
    """The ghost is a spooky being who leaves clues and hunts the player.

    Stereotype: Information Holder
    """
    def __init__(self):
        """The class constructor

        Args:
            self (Ghost): An instance of Ghost
        """
        self.cooldown_time = 0
        self.hunt_time = 0
        self.time_since_last_interaction = 0
        self.hunt_mode_on = False
        self.position = 500,500
        self.hunt_mode = Hunt_Mode()
        self.action_mode = Action_Mode()

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

        if self.cooldown_time > 30:
            self.hunt_mode_on = self.hunt_mode.hunt_check(sanity)
            self.cooldown_time -= 5 #this prevents the hunt mode from checking every second after cooldown time is greater than 30

        if self.hunt_time > 15:
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
