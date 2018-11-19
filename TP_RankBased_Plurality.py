matrix =    [ [ 3,  3,  2,  2 ],
            ['A','B','C','D'],
            ['B','C','D','A'],
            ['C','D','A','B'],
            ['D','A','B','C']
                                    ]
def pluralityElimination(matrix):
    rows, cols = len(matrix), len(matrix[0])
    score = dict.fromkeys(matrix[1], 0) 
    for c in range(cols):
        for r in range(1,rows):
            if matrix[r][c] in score:
                score[matrix[r][c]] += matrix[0][c]
                break
    maximum = max(score.values())
    for player in list(score):
        if score[player] != maximum:
            score.pop(player)
    return list(score.keys())

print(pluralityElimination(matrix))
            
    

                                