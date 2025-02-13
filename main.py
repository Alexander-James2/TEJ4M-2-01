#!/usr/bin/env python3
"""
Created by: Alex James
Created on: Feb 2025
This is "Turing Machine" program that accepts the state machine rules
    and the initial "tape" and then runs
"""

from TuringMachine import TuringMachine

## State machine for binary counting
state_machine = {
    # Move to the right until the blank space is found
    ("init", "1"): ("init", "1", "R"),
    ("init", "0"): ("init", "0", "R"),
    ("init", " "): ("add_one", " ", "L"),  # Found the end, start adding 1

    # Start binary incrementing
    ("add_one", "0"): ("final", "1", "N"),  # 0 → 1 (no carry, done)
    ("add_one", "1"): ("add_one", "0", "L"),  # 1 → 0 (carry continues)
    ("add_one", " "): ("final", "1", "L"),  # All digits were 1s, add a new 1 at the left
}

# Initial tape: 11 in binary (1011) with a blank space at the end
initial_tape = "1011 "
a_turing_machine = TuringMachine(
    initial_tape,  # Initial tape represents binary 11
    initial_state="init",
    final_states={"final"},
    transition_function=state_machine,
)

# Display input tape
print("Input on Tape:\n              " + a_turing_machine.get_tape())
print("              ▲" + "\n")

original_tape = a_turing_machine.get_tape()

# Run the Turing machine multiple times to count up to 10000 (binary 16)
for _ in range(5):  # Loop it 5 times to count up 5 times
    a_turing_machine = TuringMachine(
        a_turing_machine.get_tape() + " ",  
        initial_state="init",
        final_states={"final"},
        transition_function=state_machine,
    )

    while not a_turing_machine.final():
        a_turing_machine.step()

# prints final results 
print("\nResult of the Turing machine calculation:")
print("Original tape: " + original_tape)
print("Final tape   : " + a_turing_machine.get_tape())
print("\nDone.")