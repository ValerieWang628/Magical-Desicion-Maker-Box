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

##------------- below are for instant run-off elimination------------##
## when there is a tie, all minimum vanish together

rankMatrix4 = [ [ 2,  3,  4,  1 ],
                ['A','B','D','C'],
                ['B','C','A','A'],
                ['C','D','B','B'],
                ['D','A','C','D']
                                    ]

# the instant run-off elimination: eliminate C first, then A and B
# winner is D!


# this is a matrix w/ only one round of elimination
rankMatrix5 = [ [ 2,  4,  1,  3 ],
                ['A','B','D','D'],
                ['B','C','A','A'],
                ['C','D','B','B'],
                ['D','A','C','C']
                                    ]

# the instant run-off elimination: 
# first round: A:2, B:4, D:4;
# second round: B:6, D:4
# B wins!


# this is a template board that player sequence in each attribute 
# is organized as a bitig snake
# weights can be assigned arbitrarily to test the algorithms

rankMatrix6 = [ [ 3,  3,  2,  2 ],
                ['A','B','C','D'],
                ['B','C','D','A'],
                ['C','D','A','B'],
                ['D','A','B','C']
                                    ]

# the IRV:
# first round: C,D out
# Second round:C,D's vote given A
# A:7 B:3
# A wins

# the Borda Count:
# if preference 4-3-2-1
# A: 4+1+2+3 = 10
# B: 3+4+1+2 = 10
# C: 2+3+4+1 = 10
# D: 1+2+3+4 = 10
# final score
# A: 10 * 3
# B: 10 * 3
# C: 10 * 2
# D: 10 * 2
# A & B win with a tie
