

import copy

playerList = ['A','B','C','D']

matrix = [  [ 4,  1,  2,  3 ],
            ['A','C','A','C'],
            ['B','B','D','A'],
            ['C','D','B','B'],
            ['D','A','C','D']]

class PathIdentifier():

    @staticmethod
    def pathIdentifier(matrix, playerList):
        '''This is a helper func, calculating all two-way paths,
        later used in the smithSetFinder func. '''
        combSet = set() 
        for i in range(len(playerList)):
            for j in range(i+1,len(playerList)):
                combSet.add((playerList[i], playerList[j]))
        rows, cols = len(matrix), len(matrix[0])
        scoreList = []
        for pair in combSet:
            score = dict.fromkeys(pair, 0)
            for player in pair:
                for c in range(cols):
                    for r in range(1,rows):
                        if matrix[r][c] == player:
                            score[player] += matrix[0][c]
                            break
                        if matrix[r][c] in pair:
                            score[matrix[r][c]] += matrix[0][c]
                            break
                break
            scoreList.append(score)
        return scoreList



class PositiveBeatFinder():

    @staticmethod
    def positiveBeatFinder(matrix, playerList):
        '''this is a helper func to only count the winner in the
            pairwise battle'''
        if len(playerList) <= 1: raise Exception('Start with at least two players.')
        scoreList= PathIdentifier.pathIdentifier(matrix, playerList)
        scoreBeatList = []
        for score in scoreList:
            scoreBeat = score.copy()
            for player in scoreBeat:
                if score[player] == max(score.values()):
                    scoreBeat[player] -= sorted(score.values())[0]
                else: scoreBeat[player] = 0
            scoreBeatList.append(scoreBeat)
        return scoreBeatList

class SmithSetFinder():

    @staticmethod
    def underdogOverriderFinder(matrix,playerList):
        '''This is a helper func to identify the all-time loser, 
            and all-time winner.
            An all-time loser will never show up in smith set.
            Eliminate underdog first.
            An all-time winner is the smith set itself.
            Most of the time there might not be an all-time winner and loser.'''
        playerSet = set(playerList)
        scoreBeatList = PositiveBeatFinder.positiveBeatFinder(matrix,playerList)
        atLeastOneWin, atLeastOneLose = set(),set()
        for scoreBeat in scoreBeatList:
            for player in scoreBeat:
                if scoreBeat[player] != 0:
                    atLeastOneWin.add(player)
                else: atLeastOneLose.add(player)
        underdogSet = playerSet - atLeastOneWin
        overriderSet = playerSet - atLeastOneLose
        return underdogSet, overriderSet, scoreBeatList

    @staticmethod
    def isDominantSet(tmpSmith, playerSet, scoreBeatList):
        '''For every player in a smith-suspicious set,
            if the player is defeated by players outside the set,
            this set cannot be Smith set.'''
        overflowSet = playerSet - tmpSmith 
        for scoreBeat in scoreBeatList:
            for player in scoreBeat:
                if (player in tmpSmith
                    and scoreBeat[player] == 0 # gets defeated
                    and max(scoreBeat, key = scoreBeat.get) in overflowSet):
                    return False
        return True

    @staticmethod
    def findSmithSet(matrix, playerList):
        '''this func uses the positive defeat score to eliminate losers
            to get the smallest dominating set, aka: the smith set '''
        playerSet = set(playerList)
        underdogSet, overriderSet, scoreBeatList = SmithSetFinder.underdogOverriderFinder(matrix,playerList)
        if overriderSet != set(): return overriderSet
        else:
            playerSet -= underdogSet
            dominantContainer = []
            playerList = list(playerSet) 
            for i in range(len(playerList)):
                tmpSmith = set()
                for player in playerList[i:]:
                    tmpSmith.add(player)
                    if SmithSetFinder.isDominantSet(tmpSmith,playerSet,scoreBeatList):
                        dominantContainer.append(tmpSmith.copy())
                        break
            return min(dominantContainer, key = len) 








   


