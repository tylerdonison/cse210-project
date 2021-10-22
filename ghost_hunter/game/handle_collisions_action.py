"""Collision handler actions. Player needs to pick up instruments and interact with the ghost in order to win the game.
"""
import arcade
from arcade.sprite_list.spatial_hash import check_for_collision, check_for_collision_with_list

class Handle_Collisions_Action():
    """Handles the Collisions between player, ghost and instruments
    """
    def __init__(self, player, ghost, instruments):
        """handles the interaction between player ghost and instruments

        Args:
            player (Sprite): Player Sprite
            ghost (Sprite): Ghost Sprite
            instruments (Sprite): Instruments for the Player to interact with ghost
        """
        self.player = player.sprite
        self.ghost = ghost.sprite
        self.instruments = instruments
        self.instrument_to_ignore = None
    
    def check_collision_between_player_and_ghost(self):
        """Checks for collision between player and ghost

        Returns:
            bool: True 
        """
        new_player = self.player
        new_player.center_x += 20
        if check_for_collision(new_player, self.ghost):
            return True
        new_player.center_x -= 40
        if check_for_collision(new_player, self.ghost):
            return True
        new_player.center_x += 20
        new_player.center_y += 20
        if check_for_collision(new_player, self.ghost):
            return True
        new_player.center_y -= 40
        if check_for_collision(new_player, self.ghost):
            return True
        new_player.center_y += 20
    
    def check_collision_between_player_and_instruments(self):
        """Checks for collision between player and instructments

        Returns:
            (self): index of collisions between player and instruments
        """
        for index in range(len(self.instruments)):
            if check_for_collision(self.player, self.instruments[index]) and index != self.instrument_to_ignore:
                return index

