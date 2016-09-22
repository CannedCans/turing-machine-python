"""
A package for simulating a Turing Machine

"""

class TuringMachine:
    def __init__(self):
        """
        @type self: TuringMachine
        @rtype: None
        """
        #self.loadedTape = DataTape()
        #self.tapes = [self.loadedTape, DataTape()]
        self.loadedTape = DataTape()
        self.states = []
        self.halted = False

    def doInstruction(self, c):
        """
        @type self: TuringMachine
        @type c: str
        @rtype: None
        """
        if c == "E":
            self.loadedTape.erase()
        elif c == "R":
            self.loadedTape.shiftRight()
        elif c == "L":
            self.loadedTape.shiftLeft()
        elif c[0] == "W":
            if c[1] == "0" or c[1] == "1":
                self.loadedTape.write(int(c[1]))
            else:
                self.loadedTape.write(c[1])
        elif c[0] == "S":
            pass
        elif c[0] == "H": #Should not get called but is a valid instruction. Halting should be handled at the states
            self.halted = True
        #elif c[0] == "I": #META INSTRUCTION, LOAD TAPE AT INDEX (insert into machine)
        #    try:
        #        print("META: LOADING TAPE: " + str(c[1]))
        #        #print(id(self.loadedTape))
        #        #self.loadedTape = self.tapes[int(c[1])]
        #        #print(id(self.loadedTape))
        #    except:
        #        print("META: SEVERE ERROR LOADING TAPE")
    def runString(self, st):
        """
        Ignores the state table, simply runs the program as typed in
        @type st: str
        @rtype: None
        """
        skip = 0
        #skipInstructions = {"W": "1", "I": "1"} #
        skipInstructions = ["W"]
        for c in range(0, len(st)):
            if skip > 0:
                skip -= 1
            else:
                if st[c] in skipInstructions and c != len(st) - 1:
                    #skip += int(skipInstructions[st[c]])
                    #self.doInstruction(st[c] + st[c+1])
                    skip += 1
                    self.doInstruction(st[c] + st[c+1])
                elif st[c] in skipInstructions and c == len(st) - 1:
                    pass #To prevent any problems when a W, etc is the last line of a run program
                        #Might need additions if a multi skip is ever added
                else:
                    self.doInstruction(st[c])

    def printTape(self):
        """
        For debugging and human readable output. Prints the loaded tape
        @type self: TuringMachine
        @rtype: None
        """
        print(self.loadedTape.tape)

    def addState(self, s=[]):
        k = State(len(self.states))
        if s != []:
            for x in s:
                k.addRow(x[0], x[1][0], x[1][1], x[1][2])
        self.states.append(k)
    def executeState(self, num):
        while self.halted == False:
            #r = self.loadedTape.read()
            iSet = self.states[num].rows[self.loadedTape.read()]
            self.runString(iSet[0] + iSet[1])
            if iSet[2] != "H":
                num = iSet[2]
            else:
                self.halted = True


class DataTape:
    def __init__(self, defaultTape = [], boundedSize = -1):
        """
        Takes in an optional defaultState for the data tape to begin on.
        Takes in an optional boundedSize at which the tape will loop

        @type self: DataTape
        @type defaultTape: list
        @type boundedSize: int
        @rtype: None
        """
        self.blank = 0
        if defaultTape == []:
            defaultTape = [self.blank, self.blank, self.blank]

        self.tape= defaultTape
        self.boundedSize = boundedSize
        self.index = 1
    def extendRight(self):
        """
        @type self: DataTape
        @rtype: None
        """
        self.tape.append(self.blank)
    def extendLeft(self):
        """
        @type self: DataTape
        @rtype: None
        """
        #self.tape.reverse().append(self.blank)
        #self.tape.reverse()
        self.tape.insert(0, self.blank)
    def shiftRight(self):
        """
        @type self: DataTape
        @rtype: None
        """
        if self.index + 1 == len(self.tape) - 1:
            self.extendRight()

        self.index += 1
    def shiftLeft(self):
        """
        @type self: DataTape
        @rtype: None
        """
        if self.index - 1 == 0:
            self.extendLeft()
            self.index = 1
        else:
            self.index -= 1
    def write(self, val):
        """
        @type self: DataTape
        @type val: int
        @rtype: None
        """
        self.tape[self.index] = val
    def erase(self):
        """
        @type self: DataTape
        @rtype: None
        """
        self.tape[self.index] = self.blank
    def read(self):
        """
        @type self: DataTape
        @rtype: int | None | str
        """
        return self.tape[self.index]

class State:
    def __init__(self, stateNum):
        self.rows = {}
        self.stateNum = stateNum
    def addRow(self, symbol, writeSymbol, moveSymbol, stateNumber):
        if symbol not in self.rows:
            self.rows.update({symbol: ["W" + writeSymbol, moveSymbol, stateNumber]})

t = TuringMachine()
t.addState([[0,["1", "R", 1]], [1, ["1", "L", 2]]])
t.addState([[0, ["1", "L", 0]], [1, ["1", "R", 1]]])
t.addState([[0, ["1", "L", 1]], [1,["1","R", "H"]]])
t.executeState(0)
t.printTape()