matrix = [  [ 2,  4,  1,  3 ],
            ['A','B','D','D'],
            ['B','C','A','A'],
            ['C','D','B','B'],
            ['D','A','C','C']
                                    ]

def instantRunoffElimination(matrix, score = None):
    rows, cols = len(matrix), len(matrix[0])
    if not score: 
        score = dict.fromkeys(matrix[1], 0) 
    if len(score) == 1: return list(score.keys())[0]
    for k in score: score[k] = 0
    # destructively set all score values to zero
    for c in range(cols):
        for r in range(1,rows):
            if matrix[r][c] in score:
                score[matrix[r][c]] += matrix[0][c]
                break
    # if there is a majority winner, directly end recursion
    for player in score:
        if score[player] >= sum(score.values()) * 0.5:
            return max(score, key=score.get)
    # if no, pop the weakest
    weakest = min(score.values())
    for player in list(score):
        if score[player] == weakest:
            score.pop(player)
    if score == dict(): return "All Tie"
    if len(score) == 1: return list(score.keys())[0]
    return instantRunoffElimination(matrix, score)

print(instantRunoffElimination(matrix))



