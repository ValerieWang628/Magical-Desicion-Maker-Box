# this is a board that has one tie: A-B
rankMatrix1 = [ [ 4,  3,  2,  1 ],
                ['A','C','B','D'],
                ['C','B','D','A'],
                ['B','D','A','B'],
                ['D','A','C','C']
                                    ]

# the path is: 
# A-B: 0; A-C: 4
# D-A: 2
# B-D: 9
# C-B: 4; C-D:4

# this is a board that has two ties: C-B & C-D
rankMatrix2 = [ [ 4,  1,  3,  2 ],
                ['A','C','B','D'],
                ['C','B','D','A'],
                ['B','D','A','B'],
                ['D','A','C','C']
                                    ]

# the path is:
# A-B: 2; A-C: 8
# D-A: 2
# B-C: 0; B-D: 6
# C-D: 0

# this is a board where all candidates have different beats
rankMatrix3 = [ [ 4,  1,  2,  3 ],
                ['A','C','A','C'],
                ['B','B','D','A'],
                ['C','D','B','B'],
                ['D','A','C','D']
                                    ]

# the path is:
# A-B: 8; A-C: 2; A-D:8
# B-C: 2; B-D: 6
# C-D: 6                                    