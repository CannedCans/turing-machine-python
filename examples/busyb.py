
if __name__ == "__main__":
    from turing import *

    #Sample code for a busy beaver as should be typed in
    t = TuringMachine()
    t.addState([[0,["1", "R", 1]], [1, ["1", "L", 2]]])
    t.addState([[0, ["1", "L", 0]], [1, ["1", "R", 1]]])
    t.addState([[0, ["1", "L", 1]], [1,["1","R", "H"]]])
    t.executeState(0)
    t.printTape()
