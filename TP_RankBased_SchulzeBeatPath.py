'''
this part is:
having all the paths identified,
identify smith set
and calculate the beat path within the smith set
'''
import copy

playerList = ['A','B','C','D']
# this playerList refers to the in-competition players
# only if the player node was dragged to the playground \
# will the player show up in the list
# in this case, assume all players are dragged for complex testing purpose

matrix = [  [ 4,  1,  2,  3 ],
            ['A','C','A','C'],
            ['B','B','D','A'],
            ['C','D','B','B'],
            ['D','A','C','D']
                                    ]

def pathIdentifier(matrix, playerList):
    '''this func is a helper func, calculating all paths,
       later used in the smithSetFinder func. '''
    combSet = set() # initializing an empty set for all combinations
    for i in range(len(playerList)):
        for j in range(i+1,len(playerList)):
            combSet.add((playerList[i], playerList[j]))
    # this is to generate a pairwise set
    # all combinations provided
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
    return scoreList, combSet

def positiveBeatFinder(matrix, playerList):
    '''this is a helper func to only count the winner in the
        pairwise battle'''
    scoreList, combSet = pathIdentifier(matrix, playerList)
    scoreBeatList = []
    for score in scoreList:
        scoreBeat = score.copy()
        # this is to prevent the original score from being modified
        # scoreBeat will only record positive path
        # and set loser beat to 0
        for player in scoreBeat:
            # ties get 0 for both direction
            if score[player] == max(score.values()):
                scoreBeat[player] -= sorted(score.values())[0]
            else: scoreBeat[player] = 0
        scoreBeatList.append(scoreBeat)
    return scoreBeatList


def underdogOverriderFinder(matrix,playerList):
    '''this is a helper func to identify the all-time loser, 
        and all-time winner.
        An all-time loser will never show up in smith set.
        Eliminate underdog first.
        An all-time winner is the smith set itslf.
        Most of the time there might not be an all-time winner and loser.'''
    playerSet = set(playerList)
    scoreBeatList = positiveBeatFinder(matrix,playerList)
    atLeastOneWin, atLeastOneLose = set(),set()
    for scoreBeat in scoreBeatList:
        for player in scoreBeat:
            if scoreBeat[player] != 0:
                atLeastOneWin.add(player)
            else: atLeastOneLose.add(player)
    underdogSet = playerSet - atLeastOneWin
    overriderSet = playerSet - atLeastOneLose
    return underdogSet, overriderSet, scoreBeatList
    # returns scoreBeatList because 
    # this func has to be and will only be called in smithSetFinder once
    # so no double calling positiveBeatFinder(matrix,playerList) is needed

def isDominantSet(tmpSmith, playerSet, scoreBeatList):
    overflowSet = playerSet - tmpSmith
    for scoreBeat in scoreBeatList:
        for player in scoreBeat:
            if (player in tmpSmith
                and scoreBeat[player] == 0
                and max(scoreBeat, key = scoreBeat.get) in overflowSet):
                return False
    return True



def smithSetFinder(matrix, playerList):
    '''this func uses the positive defeat score to eliminate losers
        to get the winner set -- the smith set '''
    playerSet = set(playerList)
    underdogSet, overriderSet, scoreBeatList = underdogOverriderFinder(matrix,playerList)
    # if overriderSet != set(): return overriderSet
    playerSet -= underdogSet
    dominantContainer = []
    for _ in playerSet:
        tmpSmith = set()
        for player in playerSet:
            tmpSmith.add(player)
            if isDominantSet(tmpSmith,playerSet,scoreBeatList):
                dominantContainer.append(tmpSmith)
    return min(dominantContainer, key = len)

print(smithSetFinder(matrix,playerList))




   


