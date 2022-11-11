class State:
    rep = int('0b111111000111111000111111000111111000111111000111111000111111000', 2)
    children  = []
    max = True
    # alpha = int('-inf')
    # beta = int ('int')


    def changeBit(parent, pos, bit):
        mask = 1 << pos
        parent = (parent & ~mask) | ((bit << pos) & mask)

    def addToColumn(self,parent, col, playerColour):
        chunckShift = col * 9
        temp = 7 << chunckShift
        indexPlace = parent & temp
        position = chunckShift + indexPlace + 3

        # Modify the bit itself
        if playerColour == 'y':
            self.changeBit(parent,position, 0)
        elif playerColour == 'r':
            self.changeBit(parent,position, 1)

        # modify the index in representation
        binary = "{0:03b}".format(indexPlace + 1)  # 101
        for i in range(len(binary)):
            self.changeBit(parent,chunckShift + i, int(binary[2 - i]))

        return parent

    def findMyChildren(self):
        myChildMax = not self.max
        for i in range (7):
            child = State()
            if(self.max == True):
                child.rep = self.addToColumn(self.rep,i,'y')
                child.max = myChildMax
            else :
                child.rep = self.addToColumn(self.rep, i, 'r')
                child.max = myChildMax

            self.children.append(child)




if __name__ == '__main__':
    state = State()
    state.rep = int('0b111111000111111000111111000111111000111111000111111000111111000', 2)
    print(bin(state.rep))
    state.addToColumn(6, 'y')
    print(bin(state.rep))
