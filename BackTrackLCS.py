s = ''
t = ''

import random
import sys
sys.setrecursionlimit(10000)

def LCS_backtrack(s, t):
    nodeDict = {}
    backtrack = []
    outputString = ''
    for i in range(len(s)+1):
        nodeDict[(i,0)] = 0
    for j in range(len(t)+1):
        nodeDict[(0,j)] = 0  
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                diaganol = nodeDict[(i-1, j-1)] + 1
            else:
                diaganol = 0
            nodeMax = max(nodeDict[(i-1,j)], nodeDict[(i,j-1)], diaganol)
            nodeDict[(i,j)] = nodeMax
            if nodeMax == nodeDict[(i-1,j)] and nodeMax == nodeDict[(i,j-1)]:      
                backtrack.append(['|','->' ])
            else:
                if nodeMax == nodeDict[(i,j-1)]:
                    backtrack.append('->')
                elif nodeMax == nodeDict[(i-1,j)]:
                    backtrack.append('|')
                else:
                    backtrack.append('\\')            
            nodeDict[(i,j)] = nodeMax          
    matrix = []
    for i in range(0, len(backtrack), len(t)):
        row = backtrack[i : i+len(t)]
        matrix.append(row)
    return matrix, nodeDict

backtrackMatrix = LCS_backtrack(s, t)[0]
nodeDict = LCS_backtrack(s, t)[1]

outputString = ''
def output_LCS(backtrack, s, i, j):
    global outputString
    if i < 0 or j < 0 :
        return
    else:
        if backtrack[i][j] == ['|', '->']:
            choice = random.choice(['|', '->'])
        else:
            choice = backtrack[i][j] 
        if choice == '|':
            output_LCS(backtrack, s, i-1, j)                    
        elif choice == '->':
            output_LCS(backtrack, s, i, j-1)                    
        else:
            outputString = s[i] + outputString
            output_LCS(backtrack, s, i-1, j-1) 
output_LCS(backtrackMatrix, s, len(s)-1, len(t)-1)
print outputString       

