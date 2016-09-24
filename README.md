# turing-machine-python
A basic Turing machine written in Python.

Can run:

  -either from states (the classic Turing machine method)
  
  -a string of instructions (cannot loop as far as I know)
  
# Instructions for Use
Regardless of how you intend to use the machine, you need to initialize an instance of it
>>> import turing

>>> t=turing.TuringMachine()

If you wish to only run a string of instructions, you just need to call

>>> t.runString(str) #Valid instructions are listed below
  
If you wish to run a set of states, you must first load all states

An example might be the 3-state busy beaver program, which leaves the tape in the state [0,1,1,1,1,1,1,0]

>>> t.addState([[0,["1", "R", 1]], [1, ["1", "L", 2]]])

>>> t.addState([[0, ["1", "L", 0]], [1, ["1", "R", 1]]])

>>> t.addState([[0, ["1", "L", 1]], [1,["1","R", "H"]]])

It is a list of lists of the form [x, [a,b,c]], where x is the row number within the state, a is the character read in, b is the movement symbol to be done, and c is the next state to move to.

All the states are now loaded, we just need to indicate which state to start off on.

Since we loaded the starting state first, it is state 0. We then call t.executeState(0)

>>> t.executeState(0)

Afterwards, we should call

>>>t.printTape()

to see the final state of the tape.


# Instructions (Mnemonics)

R - Shifts the tape one to the right

L - Shifts the tape one to the left

W# - Writes the symbol in the second character to the tape where the head is, converts 1 or 0 to ints before writing

   - Does not execute the character after the W (skips it)

E - Sets the symbol below the head to the blank character

S - Skip, can be used as a valid movement to do nothing

H - Halts the program, only really useful when executing a state, otherwise does nothing

Other characters should not be executed or impact the program (including spaces) which you can use for formatting
