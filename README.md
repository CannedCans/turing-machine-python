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
An example should be the 3-state busy beaver program, which leaves the tape in the state [0,1,1,1,1,1,1,0]

# Instructions (Mnemonics)
