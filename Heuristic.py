

class Window:
    yellows = 0
    reds = 0

    def getWindowScore(self):
        if self.reds > 0 and self.yellows > 0:
            return 0
        return self.reds - self.yellows

    def addToWindow(self, input):
        if input == 'y':
            self.yellows = self.yellows + 1
        elif input == 'r':
            self.reds = self.reds + 1

    def removeFromWindow(self, out):
        if out == 'y':
            self.yellows = self.yellows - 1
        elif out == 'r':
            self.reds = self.reds - 1


class Heuristic:
    stateBoard = [[]]
    redCount = [0, 0, 0, 0, 0]
    yellowCount = [0, 0, 0, 0, 0]

    def __init__(self, board):
        self.stateBoard = board

    def updateCounters(self, partialScore):
        if partialScore > 0:
            self.redCount[partialScore] = self.redCount[partialScore] + 1
        elif partialScore < 0:
            s = partialScore * (-1)
            self.yellowCount[s] = self.yellowCount[s] + 1

    def checkLine(self, startx, starty, dx, dy):
        counter = 0
        y = starty
        x = startx
        window = Window()
        while x < len(self.stateBoard[0]) and y < len(self.stateBoard) and x >= 0 and y >= 0:
            counter = counter + 1
            window.addToWindow(self.stateBoard[y][x])
            if (counter > 4):
                window.removeFromWindow(self.stateBoard[y - 4 * dy][x - 4 * dx])
                self.updateCounters(window.getWindowScore())
            elif (counter == 4):
                self.updateCounters(window.getWindowScore())
            x = x + dx
            y = y + dy

    def checkDownwardDiagonals(self):
        for i in range(len(self.stateBoard)):
            self.checkLine(0, i, 1, -1)
        for i in range(1, len(self.stateBoard[0])):
            self.checkLine(i, len(self.stateBoard) - 1, 1, -1)


    def checkUpwardDiagonals(self):
        for i in range(len(self.stateBoard)):
            self.checkLine(0, i, 1, 1)
        for i in range(1, len(self.stateBoard[0]) ):
            self.checkLine(i, 0, 1, 1)


    def checkDiagonals(self):
        self.checkUpwardDiagonals()
        self.checkDownwardDiagonals()

    def checkRows(self):
        for i in range(0, len(self.stateBoard)):
            self.checkLine(0, i, 1, 0)

    def checkColumns(self):
        for i in range(0, len(self.stateBoard[0])):
            self.checkLine(i, 0, 0, 1)

    def getHeuristicScore(self):
        self.checkColumns()
        self.checkRows()
        self.checkDiagonals()

        weight = [0,0.05,0.015,0.45,1]
        score = 0
        score = score + self.redCount[4]*weight[4] - self.yellowCount[4]*weight[4]
        score = score + self.redCount[3]*weight[3] - self.yellowCount[3]*weight[3]
        score = score + self.redCount[2]*weight[2] - self.yellowCount[2]*weight[2]
        score = score + self.redCount[1]*weight[1] - self.yellowCount[1]*weight[1]
        return -1* score


if __name__ == '__main__':
    board = []
    board.insert(0, ['w', 'w', 'w', 'w', 'w', 'w', 'y'])
    board.insert(0, ['w', 'w', 'w', 'w', 'w', 'w', 'w'])
    board.insert(0, ['w', 'w', 'w', 'w', 'w', 'w', 'w'])
    board.insert(0, ['w', 'w', 'w', 'w', 'w', 'w', 'w'])
    board.insert(0, ['y', 'w', 'w', 'w', 'w', 'w', 'w'])
    board.insert(0, ['r', 'r', 'r', 'r', 'r', 'r', 'r'])

    h = Heuristic( board)
    h.getHeuristicScore()

