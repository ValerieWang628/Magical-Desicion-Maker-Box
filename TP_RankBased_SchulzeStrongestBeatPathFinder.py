import schulzeBeat
import copy
import math

matrix = [ [ 2,  4,  1,  3 ],
            ['A','B','D','D'],
            ['B','C','A','A'],
            ['C','D','B','B'],
            ['D','A','C','C']
                                ]
playerList = ['A','B','C','D']

scoreBeatList = schulzeBeat.PositiveBeatFinder().positiveBeatFinder(matrix, playerList)
smithSet = schulzeBeat.SmithSetFinder().findSmithSet(matrix, playerList)



def smithSetExcluder(scoreBeatList, smithSet):
    for score in scoreBeatList.copy():
        if not ((set(score.keys()) <= smithSet)):
            scoreBeatList.remove(score)
    return scoreBeatList

def viableRouteFinder(node1, node2, scoreBeatList, smithSet):
    routeList = routeGenerator(node1, node2, smithSet)
    for route in routeList.copy():
        if not isViable(route, scoreBeatList, smithSet):
            routeList.remove(route)
    return routeList

def strongestPathFinder(node1, node2, scoreBeatList, smithSet):
    strongestPath = []
    routeList = viableRouteFinder(node1, node2, scoreBeatList, smithSet)
    beatPath = []
    for route in routeList:
        weakest = getWeakestLink(route, scoreBeatList)
        beatPath.append((route, weakest))
    strongest = 0
    for pair in beatPath:
        if pair[1] >= strongest:
            strongest = pair[1]
    for pair in beatPath:
        if pair[1] == strongest:
            strongestPath.append(pair[0])
    return strongestPath


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


def isViable(route, scoreBeatList, smithSet):
    if not oneWayConnectable(route[-1], route[0], scoreBeatList, smithSet):
        return False
    for i in range(len(route)-1):
        if not oneWayConnectable(route[i], route[i+1], scoreBeatList, smithSet):
            return False
    return True

def oneWayConnectable(node1, node2, scoreBeatList, smithSet):
    scoreBeatList = smithSetExcluder(scoreBeatList, smithSet)
    for score in scoreBeatList:
        if (node1 in score
            and node2 in score
            and score[node1] != 0):
            return True
    return False

def routeGenerator(node1, node2, smithSet):
    connector = smithSet - {node1, node2}
    maxSpace = len(smithSet) - 2
    route = []
    route.append([node1, node2])
    for i in range(maxSpace):
        space = [-1] * (i+1)
        template = [node1] + space + [node2]
        for _ in range(math.factorial(maxSpace)//math.factorial(maxSpace-(i+1))):
            filler(template.copy(), connector, route, i)
    return route
        
def isFull(template):
    if -1 not in template: return True
    return False

def filler(template, connector, route, ind):
    if isFull(template):
        return template
    else:
        for joint in connector:
            for i in range(len(template) - 1):
                if (template[i] == -1
                    and joint not in template):
                    template[i] = joint
                    if (template not in route):
                        if isFull(template):
                            route.append(template)
                            return template
                        elif filler(template, connector, route, ind+1):
                            return template
                    template[i] = -1
    return None

