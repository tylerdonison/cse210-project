""" This class interacts with actors to change the state of the game. Code taken from action.py file in Robot Finds Kitten"""
class Action:
    """The class Action which uses execute 
  
    Stereotype:
        Controller
    """
    def execute(self, cast):
        """Executes the action using the given actors
        
        Args:
            cast(dict): the game actors
        """
        raise NotImplementedError("execute not implemented in superclass")
