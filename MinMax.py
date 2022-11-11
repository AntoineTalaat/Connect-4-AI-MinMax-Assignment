import State


class MinMax:

    def buildKLevels(self, k, currentState):
        if k != 0:
            currentState.findMyChildren()
            k = k - 1
            for i in range(len(currentState.children)):
                self.buildKLevels(k, currentState.children[i])

    def maxValue(self, state):
        v = float('-inf')
        for child in state.children:
            value = self.MinMax(k - 1, child, withAlphaBeta)
            if value > v:
                v = value
                move = child
        return v, move

    def minValue(self, state):
        v = float('inf')
        for child in state.children:
            value = self.MinMax(k - 1, child, withAlphaBeta)
            if value < v:
                v = value
                move = child
        return v, move

    def MinMax(self, k, currentState, withAlphaBeta):
        self.buildKLevels(k, currentState)
        if k == 0:
            return currentState.getScore()
        if currentState.max:
            v, move = minValue(currentState)
        else:
            v, move = maxValue(currentState)

        return move
