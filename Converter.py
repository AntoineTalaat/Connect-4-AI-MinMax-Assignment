class Converter:
    def convertStateToArray(self, state):
        rows, cols = (6, 7)
        arrayState = [['white' for i in range(cols)] for j in range(rows)]
        state = str(state)
        index = 0
        col = 0
        while col != 7:
            print(state[index: index+3])
            emptyIndex = int(state[index: index+3], 2)  # convert binary rep of empty space to decimal

            if emptyIndex != 0:
                for i in range(0, emptyIndex - 1):
                    print("d5alt")
                    if state[index + i] == '0':
                        arrayState[i][col] = 'yellow'
                    else:
                        arrayState[i][col] = 'red'
            index = index + emptyIndex + 2
            col = col + 1
            for row in arrayState:
                print(row)
        return arrayState


if __name__ == '__main__':
    conv = Converter()
    arr = conv.convertStateToArray(101110001010000100100001000000)





