
import math
import copy

matrix = [ [ 2,  4,  1,  3 ],
            ['A','B','D','D'],
            ['B','C','A','A'],
            ['C','D','B','B'],
            ['D','A','C','C']
                                ]
playerList = ['A','B','C','D']

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


class StrongestPathFinder():

    @staticmethod
    def smithSetExcluder(scoreBeatList, smithSet):
        for score in scoreBeatList.copy():
            if not ((set(score.keys()) <= smithSet)):
                scoreBeatList.remove(score)
        return scoreBeatList

    @staticmethod  
    def viableRouteFinder(node1, node2, scoreBeatList, smithSet):
        routeList = StrongestPathFinder.routeGenerator(node1, node2, smithSet)
        for route in routeList.copy():
            if not StrongestPathFinder.isViable(route, scoreBeatList, smithSet):
                routeList.remove(route)
        return routeList

    @staticmethod
    def strongestPathFinder(node1, node2, scoreBeatList, smithSet):
        strongestPath = []
        routeList = StrongestPathFinder.viableRouteFinder(node1, node2, scoreBeatList, smithSet)
        beatPath = []
        for route in routeList:
            weakest = StrongestPathFinder.getWeakestLink(route, scoreBeatList)
            beatPath.append((route, weakest))
        strongest = 0
        for pair in beatPath:
            if pair[1] >= strongest:
                strongest = pair[1]
        for pair in beatPath:
            if pair[1] == strongest:
                strongestPath.append(pair[0])
        return strongestPath

    @staticmethod
    def getWeakestLink(route, scoreBeatList):
        weakest = 0
        for score in scoreBeatList:
            if (route[0] in score
                and route[-1] in score):
                if score[route[0]] != 0:
                    weakest = score[route[0]]
                else: weakest = score[route[-1]]
        for i in range(len(route)-1):
            confront, rival = route[i], route[i+1]
            for score in scoreBeatList:
                if (confront in score
                    and rival in score):
                    if (score[confront] != 0
                        and score[confront] < weakest):
                        weakest = score[confront]
                    elif (score[rival] != 0
                        and score[rival] < weakest):
                        weakest = score[rival]
        return weakest

    @staticmethod
    def isViable(route, scoreBeatList, smithSet):
        if not StrongestPathFinder.oneWayConnectable(route[-1], route[0], scoreBeatList, smithSet):
            return False
        for i in range(len(route)-1):
            if not StrongestPathFinder.oneWayConnectable(route[i], route[i+1], scoreBeatList, smithSet):
                return False
        return True

    @staticmethod
    def oneWayConnectable(node1, node2, scoreBeatList, smithSet):
        scoreBeatList = StrongestPathFinder.smithSetExcluder(scoreBeatList, smithSet)
        for score in scoreBeatList:
            if (node1 in score
                and node2 in score
                and score[node1] != 0):
                return True
        return False

    @staticmethod
    def routeGenerator(node1, node2, smithSet):
        connector = smithSet - {node1, node2}
        maxSpace = len(smithSet) - 2
        route = []
        route.append([node1, node2])
        for i in range(maxSpace):
            space = [-1] * (i+1)
            template = [node1] + space + [node2]
            for _ in range(math.factorial(maxSpace)//math.factorial(maxSpace-(i+1))):
                StrongestPathFinder.filler(template.copy(), connector, route, i)
        return route

    @staticmethod        
    def isFull(template):
        if -1 not in template: return True
        return False

    @staticmethod
    def filler(template, connector, route, ind):
        if StrongestPathFinder.isFull(template):
            return template
        else:
            for joint in connector:
                for i in range(len(template) - 1):
                    if (template[i] == -1
                        and joint not in template):
                        template[i] = joint
                        if (template not in route):
                            if StrongestPathFinder.isFull(template):
                                route.append(template)
                                return template
                            elif StrongestPathFinder.filler(template, connector, route, ind+1):
                                return template
                        template[i] = -1
        return None

