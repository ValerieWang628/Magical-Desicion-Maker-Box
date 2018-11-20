'''
------ this the description of Schulze's Beat Path Method in Wikipedia------
source: https://en.wikipedia.org/wiki/Schulze_method

The Schulze method is an electoral system 
developed in 1997 by Markus Schulze 
that selects a single winner using votes 
that express preferences. 
The method can also be used to create 
a sorted list of winners. 
The Schulze method is also known as 
Schwartz Sequential dropping (SSD), 
the beatpath method, 
beatpath winner, 
path voting, 
and path winner.

The Schulze method is a Condorcet method, 
which means that if there is a candidate 
who is preferred by a majority 
over every other candidate 
in pairwise comparisons, 
then this candidate will be the winner 
when the Schulze method is applied.

The output of the Schulze method (defined below) 
gives an ordering of candidates. 
Therefore, if several positions are available, 
the method can be used for this purpose without modification, 
by letting the k top-ranked candidates win the k available seats. 
Furthermore, for proportional representation elections, 
a single transferable vote variant has been proposed.

'''

'''
source: https://en.wikipedia.org/wiki/Smith_set

In voting systems, the Smith set, named after John H. Smith, 
but also known as the top cycle, or as GETCHA, 
is the smallest non-empty set of candidates 
in a particular election such that 
each member defeats every other candidate 
outside the set in a pairwise election. 
The Smith set provides one standard of optimal choice 
for an election outcome. 
Voting systems that always elect a candidate 
from the Smith set 
pass the Smith criterion 
and are said to be "Smith-efficient".

A set of candidates where every member of the set 
pairwise defeats every member outside of the set 
is known as a dominating set.

'''

'''
this part of the code is:
with all the paths identified 
(note: both directions, such as A beats B by 2, B beats A by 3),
- calculate the pairwise winners' path strength by the positiveBeatFinder function,
(note: only one direction, such as B defeats A by 1 (3 - 2 = 1)),
- identify smith set,
and 
- calculate the beat path within the smith set
- get the final winner
'''

import copy

# playerList = ['A','B','C','D']
playerList = ['B','C','D']
# playerList = ['B']

# This playerList refers to the in-competition players
# Only if the player node was dragged to the playground \
# will the player show up in the list.
# In this case, assume all players are dragged for complex testing purpose.

matrix = [  [ 4,  1,  2,  3 ],
            ['A','C','A','C'],
            ['B','B','D','A'],
            ['C','D','B','B'],
            ['D','A','C','D']
                                    ]

def pathIdentifier(matrix, playerList):
    '''This is a helper func, calculating all two-way paths,
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
    if len(playerList) <= 1: raise Exception('Start with at least two players.')
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


print(positiveBeatFinder(matrix,playerList))

def underdogOverriderFinder(matrix,playerList):
    '''This is a helper func to identify the all-time loser, 
        and all-time winner.
        An all-time loser will never show up in smith set.
        Eliminate underdog first.
        An all-time winner is the smith set itself.
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
    '''For every player in a smith-suspicious set,
        if the player is defeated by players outside the set,
        this set cannot be Smith set.'''
    overflowSet = playerSet - tmpSmith # outside the smith-suspicious set
    for scoreBeat in scoreBeatList:
        for player in scoreBeat:
            if (player in tmpSmith
                and scoreBeat[player] == 0 # gets defeated
                and max(scoreBeat, key = scoreBeat.get) in overflowSet):
                return False
    return True



def smithSetFinder(matrix, playerList):
    '''this func uses the positive defeat score to eliminate losers
        to get the smallest dominating set, aka: the smith set '''
    playerSet = set(playerList)
    underdogSet, overriderSet, scoreBeatList = underdogOverriderFinder(matrix,playerList)
    if overriderSet != set(): return overriderSet
    # If there is an ovverrider set,
    # it must have only one object in the set,
    # unless there are ties in the set that defeats all outsiders.
    # The overrider set is the absolute smith set
    else:
        playerSet -= underdogSet
        dominantContainer = []
        playerList = list(playerSet) 
        # This list differs from the original in-play set 
        # in that it eliminates underdog. 
        # Thus reduces unnecessary iterations
        for i in range(len(playerList)):
            tmpSmith = set()
            # every time the new empty smith set starts from a player
            for player in playerList[i:]:
            # this guarantees that the player will never be visited twice
                tmpSmith.add(player)
                if isDominantSet(tmpSmith,playerSet,scoreBeatList):
                    dominantContainer.append(tmpSmith.copy())
                    break
                    # the tmpSmith length grows ascendingly
                    # so once tmpSmith satisfies a dominating set
                    # no more player adding is needed
        return min(dominantContainer, key = len) # get the smallest set

