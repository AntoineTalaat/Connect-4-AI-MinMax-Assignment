import State
class MinMax:

    def buildKLevels(self,k,currentState):
        if(k!=0):
            currentState.findMyChildren()
            k=k-1
            for i in range (len(currentState.children)):
                self.buildKLevels(k, currentState.children[i])



    def MinMax (self,k , currentState , withAlphaBeta):
        self.buildKLevels(k,currentState)


