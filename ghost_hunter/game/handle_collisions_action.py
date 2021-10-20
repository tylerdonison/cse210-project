import arcade
from arcade.sprite_list.spatial_hash import check_for_collision

class Handle_Collisions_Action():
    def __init__(self, player, ghost):
        self.player = player.sprite
        self.ghost = ghost.sprite
    
    def check_collision(self):
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
    

