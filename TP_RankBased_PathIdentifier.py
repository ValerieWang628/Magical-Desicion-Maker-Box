'''
this part is:
given a list of all candidates and the matrix w/ weights
the program calculates all the pairwise beats and put the paths in a dictionary,
stored in a list.
Note that, both directions are included. 
To identify the direction, have to see which key's value is bigger.
Later in the matrix drawing, red identifies negative, while green for positive.
'''

playerList = ['A','B','C','D']

s = set()
# this is to generate a pairwise set
# all combinations provided
for i in range(len(playerList)):
    for j in range(i+1,len(playerList)):
        s.add((playerList[i], playerList[j]))

# print(s)

matrix = [  [ 4,  1,  2,  3 ],
            ['A','C','A','C'],
            ['B','B','D','A'],
            ['C','D','B','B'],
            ['D','A','C','D']
                                    ]

rows, cols = len(matrix), len(matrix[0])
l = []
for pair in s:
    score = dict.fromkeys(pair, 0)
    for p in pair:
        for c in range(cols):
            for r in range(1,rows):
                if matrix[r][c] == p:
                    score[p] += matrix[0][c]
                    break
                if matrix[r][c] in pair:
                    score[matrix[r][c]] += matrix[0][c]
                    break
        break
    l.append(score)

print(l)
