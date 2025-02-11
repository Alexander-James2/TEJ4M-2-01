"""
Created by: Mr. Coxall
Created on: Sept 2020

TuringMachine.py

This module contains the TuringMachine class which simulates a Turing Machine.

Classes:
--------
TuringMachine : A class to represent a Turing Machine.
"""

import time
from Tape import Tape


class TuringMachine(object):
    """
    A class to represent a Turing Machine.

    Attributes:
    ----------
    tape : str
        The initial tape content.
    blank_symbol : str
        The symbol representing a blank space on the tape.
    initial_state : str
        The initial state of the Turing Machine.
    final_states : list
        A list of final states of the Turing Machine.
    transition_function : dict
        A dictionary representing the transition function of the Turing Machine.
    """

    def __init__(
        self,
        tape="",
        blank_symbol=" ",
        initial_state="",
        final_states=None,
        transition_function=None,
    ):
        """
        Constructs all the necessary attributes for the Turing Machine object.

        Parameters:
        ----------
        tape : str, optional
            The initial tape content (default is an empty string).
        blank_symbol : str, optional
            The symbol representing a blank space on the tape (default is a space).
        initial_state : str, optional
            The initial state of the Turing Machine (default is an empty string).
        final_states : list, optional
            A list of final states of the Turing Machine (default is None).
        transition_function : dict, optional
            A dictionary representing the transition function of the Turing Machine (default is None).
        """
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        """
        Returns the current content of the tape as a string.

        Returns:
        -------
        str
            The current content of the tape.
        """
        return str(self.__tape)

    def step(self):
        """
        Executes one step of the Turing Machine based on the current state and the symbol under the head.

        The method updates the tape, moves the head, and changes the state of the Turing Machine
        according to the transition function.
        """
        char_under_head = self.__tape[self.__head_position]
        current_state_and_symbol = (self.__current_state, char_under_head)
        if current_state_and_symbol in self.__transition_function:
            transition = self.__transition_function[current_state_and_symbol]
            self.__tape[self.__head_position] = transition[1]
            if transition[2] == "R":
                self.__head_position += 1
                print("  ↣ Move head 1 right")
            elif transition[2] == "L":
                self.__head_position -= 1
                print("  ↢ Move head 1 left")
            self.__current_state = transition[0]
            print("             ", end="")
            for head_position_counter in range(self.__head_position):
                print(" ", end="")
            print("▲\n")
            time.sleep(1.0)

    def final(self):
        """
        Checks if the current state of the Turing Machine is a final state.

        Returns:
        -------
        bool
            True if the current state is a final state, False otherwise.
        """
        return self.__current_state in self.__final_states
