class MinMax:
    def maxValue(self, k, state, withAlphaBeta):
        v = float('-inf')
        move = None
        children = state.findMyChildren()
        for child in children:
            value, futureMove = self.MinMax(k - 1, child, withAlphaBeta, False)
            if value > v:
                v = value
                move = child
            if withAlphaBeta and value >= state.beta:
                return (value, move)
            if withAlphaBeta:
                state.beta = max(state.alpha, value)
        return (v, move)

    def minValue(self, k, state, withAlphaBeta):
        v = float('inf')
        move = None
        children = state.findMyChildren()
        for child in children:
            value, futureMove = self.MinMax(k - 1, child, withAlphaBeta, True)
            if value < v:
                v = value
                move = child
            if withAlphaBeta and v <= state.alpha:
                return v, move
            if withAlphaBeta:
                state.beta = min(state.beta, v)

        return (v, move)

    def MinMax(self, k, currentState, withAlphaBeta, isAITurn):
        if k == 0:
            return currentState.getScore(), currentState
        if not isAITurn:
            v, move = self.minValue(k, currentState, withAlphaBeta)
        else:
            v, move = self.maxValue(k, currentState, withAlphaBeta)
        return v, move
