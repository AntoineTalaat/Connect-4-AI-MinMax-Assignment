class Converter:

    def convertStateToArray(self,inState:int):
        state = "{0:b}".format(inState)
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
        print("e7na fi el bta3 da ")
        for row in arr:
            print(row)
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
        print("representation :" , representation)   
        representation = int(representation,2)
        return representation
