"""
Tape.py

This module contains the Tape class which simulates the tape of a Turing Machine.

Classes:
--------
Tape : A class to represent a Turing Machine tape.
"""


class Tape(object):
    """
    A class to represent a Turing Machine tape.

    Attributes:
    ----------
    blank_symbol : str
        The symbol representing a blank space on the tape.
    """

    blank_symbol = " "

    def __init__(self, tape_string=""):
        """
        Constructs all the necessary attributes for the Tape object.

        Parameters:
        ----------
        tape_string : str, optional
            The initial content of the tape (default is an empty string).
        """
        self.__tape = dict((enumerate(tape_string)))

    def __str__(self):
        """
        Returns the current content of the tape as a string.

        Returns:
        -------
        str
            The current content of the tape.
        """
        tape_content = ""
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for position in range(min_used_index, max_used_index):
            tape_content += self.__tape[position]
        return tape_content

    def __getitem__(self, index):
        """
        Returns the symbol at the given position on the tape.

        Parameters:
        ----------
        index : int
            The position on the tape.

        Returns:
        -------
        str
            The symbol at the given position.
        """
        return self.__tape.get(index, Tape.blank_symbol)

    def __setitem__(self, pos, char):
        """
        Sets the symbol at the given position on the tape.

        Parameters:
        ----------
        pos : int
            The position on the tape.
        char : str
            The symbol to set at the given position.
        """
        print("Write: " + char + " at position: " + str(pos))
        self.__tape[pos] = char
        print("Current tape: ", end="")
        for key, value in self.__tape.items():
            print(value, end="")
