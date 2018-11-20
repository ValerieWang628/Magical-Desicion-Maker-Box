'''
This func is for Borda Voting.
Given a matrix, first transform it to a 2D list with a dataframe-like structure
and fill all the values with 0, except for the weight row and alternative column.
Then loop thru the original matrix, according to the borda preference the user assigned,
the first place gets whatever score the user assigned to the first place. 
The second place gets the score assigned for the second.
Later, all the alternatives get their rank borda score for each attribute.
Sumproduct weight and rank borda score, 
the function returns a dictionary with the final weighted score of each alternatives.
'''

import copy

matrix = [      [ 3,  3,  2,  2 ],
                ['A','B','C','D'],
                ['B','C','D','A'],
                ['C','D','A','B'],
                ['D','A','B','C']
                                    ]
bordaPreference = [4,3,2,1]

playerSet = {'A','B','C','D'}
assert(len(bordaPreference) == len(matrix[0]))


def matrix2Dtransformer(matrix, playerSet):
    playerList = list(playerSet)
    # convert the set to list so that the order doesn't change
    altMatrix = copy.deepcopy(matrix)
    header = ["ph"] + altMatrix[0] 
    # ph is just for placeholder
    # this maintains the rectangular shape
    altMatrix[0] = header
    rows, cols = len(matrix), len(matrix[0])
    for r in range(1,rows):
        altMatrix[r] = [0]*len(altMatrix[r])
        # replace aternatives to zero 
        # so that later be filled with rank score
        altMatrix[r].insert(0,playerList[r-1])
        # add alternative to the first column
        # notice the order is based on the playerList's index
    return altMatrix,playerList

def bordaCount(matrix, playerSet,bordaPreference):
    altMatrix, playerList = matrix2Dtransformer(matrix, playerSet)
    rows, cols = len(matrix), len(matrix[0])
    for c in range(cols):
        for r in range(1, rows):
            targetRow = playerList.index(matrix[r][c])
            altMatrix[targetRow+1][c+1] = bordaPreference[r-1]
            # to link the place with the new row index in the altMatrix
            # then assign the corresponding rank borda score to the target
    rows, cols = len(altMatrix), len(altMatrix[0])
    score = dict.fromkeys(playerList, 0) 
    for r in range(1,rows):
        for c in range(1,cols):
            score[altMatrix[r][0]] += altMatrix[r][c] * altMatrix[0][c]
            # sumproduct the borda score row and the attribute weight row
    return score


print(bordaCount(matrix,playerSet,bordaPreference))

