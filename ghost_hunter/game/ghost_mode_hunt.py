"""This module is in charge of controlling the hunt mode of the ghost"""
import random
import arcade

class Hunt_Mode:
    def __init__(self, player):
        self.physics_engine = None
        self.scene = None
        self.target = player
        

    def hunt(self, player_sprite, ghost_sprite, wall_list):
        """Causes the ghost to hunt the player. This means that the ghost moves towards the player
        """
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.target.sprite, self.scene.get_sprite_list("Front Door")) #lock front door
        #add sound to indicate locked door
        
        if arcade.has_line_of_sight(player_sprite.position,
                                            ghost_sprite.position,
                                            wall_list):
           self.follow_sprite()
       
        #make ghost appear
        #move towards person if in line of sight
        #if the person is not in line of sight. Move randomly





    
    def hunt_check(self, sanity):
        """Checks to see if the ghost will hunt the player. There is a 1 in 20 chance of being hunted if they have 100 sanity
        and a 1 in 1 chance if their sanity gets to 5

        Args:
            sanity (int): The ammount of sanity that the player has.

        """

        #This ensures that the chance of being hunted will never be greater than a 1 in 1 chance (prevent bugs)
        if sanity < 5:
            sanity = 5 #Remember that this won't change sanity globally. Just don't pass in sanity as a number instead of accessing it through an object

        
        chance_of_being_hunted_inverse = int(sanity / 5)
        round(chance_of_being_hunted_inverse) #ensures that the chance of being hunted will be an int

        #creates a list from 1 to the inverse of the chance of being hunted. (A greater number is better for the player). Then randomly chooses a number
        #from the list. If it is a one, they will be hunted. Chances of having a 1 increase with a smaller list.
        chance_list = []
        for i in range(chance_of_being_hunted_inverse):
            chance_list.append(i + 1)

        random_number_in_chance_list = random.choice(chance_list)
        if random_number_in_chance_list == 1:
            ghost_hunt_mode = True
        else:
            ghost_hunt_mode = False
        return ghost_hunt_mode #This will probably need to be changed to an object that is passed in
    
    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the Ghost
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the Ghost to the destination.
            # Calculate the angle in radians between the start points
            # and end points. This is the angle the Ghost will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the Ghost travels.
            self.change_x = math.cos(angle) * GHOST_SPEED
            self.change_y = math.sin(angle) * GHOST_SPEED
