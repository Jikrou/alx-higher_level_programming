#!/usr/bin/python3
""" A module define a LockedClass """


class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.

    Attributes:
        None

    Methods:
        __setattr__(self, name, value): Overrides the default setattr behavior
        to allow setting  only the 'first_name' attribute dynamically.
    """

    def __setattr__(self, name, value):
        """
        Overrides the default setattr behavior to allow setting only the
        'first_name' attribute dynamically.

        Args:
            name (str): The name of the attribute being set.
            value (any): The value to assign to the attribute.

        Raises:
            AttributeError: If the attribute being set is not 'first_name'.
        """
        if name != 'first_name':
            err_msg = "Cannot add new attributes except 'first_name'"
            raise AttributeError(err_msg)
        self.__dict__[name] = value
