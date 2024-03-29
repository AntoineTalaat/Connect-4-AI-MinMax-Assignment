class Converter:

    def convertStateToArray(self,inState:int):
        state = "{0:b}".format(inState)
        if(len(state) < 63):
            for i in range(63 - len(state)):
                state = "0" + state
        rows, cols = (6, 7)
        arrayState = [['w' for i in range(cols)] for j in range(rows)]
        state = str(state)
        index = len(state)
        col = 0
        while col != 7:
            nextIndex = int(state[index - 3: index], 2)  # convert binary rep of empty space to decimal
            i = 0
            startIndex = index - 4
            while nextIndex != 0:
                if state[startIndex] == '0':
                    arrayState[i][col] = 'y'
                else:
                    arrayState[i][col] = 'r'
                startIndex = startIndex - 1
                i = i + 1
                nextIndex = nextIndex - 1

            index = index - 9
            col = col + 1

        return arrayState

    def convertArrayToState(self, arr):
        representation = ""
        rows = len(arr)
        columns = len(arr[0])
        for j in range(columns-1,-1,-1):
            index = 6
            for i in range(rows):
                if arr[i][j] == 'w':
                    index = i
                    break

            binary = "{0:03b}".format(index)
            for x in range(rows-1,-1,-1):
                if arr[x][j] == 'y':
                    representation += "0"
                else:
                    representation += "1"
            representation += binary
        representation = int(representation,2)
        return representation

    def convertStateToString(self, rep):
        state = "{0:b}".format(rep)
        if (len(state) < 63):
            for i in range(63 - len(state)):
                state = "0" + state
        stringState = ""
        for i in range(7):
            index = i * 9
            stringState = stringState + state[index: index+6] + "(" + state[index+6: index+9] + ")-"

        stringState = stringState[0: len(stringState) - 1]
        return stringState
