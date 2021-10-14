
#will only hunt if player's sanity is below 50, when hunt check passes, it will activate hunt phase.

import random

def hunt_check(sanity):
    """Checks to see if the ghost will hunt the player. There is a 1 in 20 chance of being hunted if they have 100 sanity
    and a 1 in 1 chance if their sanity gets to 5

    Args:
        sanity (int): The ammount of sanity that the player has.

    """

    #This ensures that the chance of being hunted will never be greater than a 1 in 1 chance (prevent bugs)
    if sanity < 5:
        sanity = 5 #Remember that this won't change sanity globally. Just don't pass in sanity as a number instead of accessing it through an object

    
    chance_of_being_hunted_inverse = sanity / 5
    round(chance_of_being_hunted_inverse) #ensures that the chance of being hunted will be an int

    #creates a list from 1 to the inverse of the chance of being hunted. (A greater number is better for the player). Then randomly chooses a number
    #from the list. If it is a one, they will be hunted. Chances of having a 1 increase with a smaller list.
    chance_list = []
    for i in range(chance_of_being_hunted_inverse):
        chance_list.append(i + 1)

    random_number_in_chance_list = random.choice(chance_list)
    if random_number_in_chance_list == 1:
        ghost_hunt_mode = True #This will probably need to be changed to an object that is passed in
    
