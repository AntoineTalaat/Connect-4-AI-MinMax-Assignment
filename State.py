class State:
    rep = int('0b111111000111111000111111000111111000111111000111111000111111000', 2)

    # alpha = int('-inf')
    # beta = int ('int')

    def changeBit(self, pos, bit):
        mask = 1 << pos
        self.rep = (self.rep & ~mask) | ((bit << pos) & mask)

    def addToColumn(self, col, playerColour):
        chunckShift = col * 9
        temp = 7 << chunckShift
        indexPlace = self.rep & temp
        position = chunckShift + indexPlace + 3

        # Modify the bit it self
        if playerColour == 'y':
            self.changeBit(position, 0)
        elif playerColour == 'r':
            self.changeBit(position, 1)

        # modify the index in representation
        binary = "{0:03b}".format(indexPlace + 1)  # 101
        for i in range(len(binary)):
            self.changeBit(chunckShift + i, int(binary[2 - i]))


if __name__ == '__main__':
    state = State()
    state.rep = int('0b111111000111111000111111000111111000111111000111111000111111000', 2)
    print(bin(state.rep))
    state.addToColumn(6, 'y')
    print(bin(state.rep))
