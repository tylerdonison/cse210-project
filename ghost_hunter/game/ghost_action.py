
Class ghost_action:
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in superclass")
