"""This is the module in charge of controlling the ghost
"""
import random
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
        self.timer = 0 #note that this timer will not count while the ghost is hunting
        self.cooldown_time = 0
        self.hunt_time = 0
        self.hunt_mode_on = False
        self.position = 500,500
        self.hunt_mode = Hunt_Mode()
        self.action_mode = Action_Mode()
        self.hunt_duration = 15
        self.max_cooldown_time = 30

    def execute(self,sanity):
        """This executes all of the updates and actions that the ghost object should have during
        each cycle.

        Args: 
            self (Ghost): An instance of Ghost
            sanity (int): the player's current sanity
        """
        self.update_time_and_status(sanity)
        self.do_hunt()

    def update_time_and_status(self,sanity):
        """This method updates the cooldown time or, if the ghost is hunging, the hunt time.

        Args: 
            self (Ghost): An instance of Ghost
            sanity (int): the player's current sanity
        """
        if self.hunt_mode_on == True:
            self.hunt_time += 1
            self.cooldown_time = 0
        else:
            self.cooldown_time +=1
            self.choose_ghost_action(sanity)

        if self.hunt_time > self.hunt_duration:
            self.hunt_mode_on == False
            self.hunt_time = 0

    def choose_ghost_action(self,sanity):
        """This method causes the ghost to do one of three things. There is a 20 percent chance that it will
        cause a hunt check, a 40 percent chance it will do nothing, and a 40 percent chance that it will leave 
        a clue. This method is executed every 10 seconds. The ghost will not hunt if the cooldown timer has not
        expired. This method should not be executed while the ghost is in hunt mode.

        Args:
            self (Ghost): An instance of Ghost
            sanity (int): the player's current sanity
        """
        self.timer += 1
        probability = [1,2,3,4,5,6,7,8,9,10]

        if self.timer % 10 == 0:
            random_decision = random.choice(probability)
            if (random_decision < 3) and (self.cooldown_time > self.max_cooldown_time) and (sanity < 51):
                self.hunt_mode_on = self.hunt_mode.hunt_check(sanity)
            elif (random_decision > 6):
                self.action_mode.cause_ghost_interaction()


    def do_hunt(self):
        """If hunt_mode is active, this will cause the ghost to hunt the player.

        Args:
            self (Ghost): An instance of Ghost
        """
        if self.hunt_mode_on == True:
            self.hunt_mode.hunt()

    def move_ghost(self):
        pass
