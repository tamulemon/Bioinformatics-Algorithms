protein1 = 'GTAGGCTTAAGGTTA'
protein2 = 'TAGATA'
indelPenalty = -5
matrix = '''
   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10
'''
import random
import sys
sys.setrecursionlimit(10000)

def PAM250_matrix(matrix):
    lst = list(matrix.split())
    lst.insert(0,' ')
    byRow = []
    PAM250Dict = {}
    for i in range(0, len(lst), 21):
        byRow.append(lst[i:i+21])
    for j in range(1, 21):
        for k in range(1, 21):
            PAM250Dict[(byRow[0][k], byRow[j][0])] = int(byRow[j][k])
    return PAM250Dict
PAM250Matrix = PAM250_matrix(matrix)
  
def LCS_backtrack_local_allignment(PAM250Matrix, indelPenalty, protein1, protein2):
    backtrack = []
    nodeDict = {}
    outputString = ''
    maxScore = 0
    startBoarder = []
    endBoarder = ''
    for i in range(len(protein1)+1):
        nodeDict[(i,0)] = indelPenalty * i
    for j in range(len(protein2)+1):
        nodeDict[(0,j)] = indelPenalty * j
    for i in range(1,len(protein1)+1):
        for j in range(1,len(protein2)+1):
            diaganol = nodeDict[(i-1, j-1)] + PAM250Matrix[(protein1[i-1], protein2[j-1])] 
            insertion = nodeDict[(i, j-1)] + indelPenalty
            deletion = nodeDict[(i-1, j)] + indelPenalty
            nodeMax = max(diaganol, insertion, deletion, 0)
            nodeDict[(i,j)] = nodeMax
            if nodeMax > maxScore:
                maxScore = nodeMax
                endBoarder = (i,j)
            if nodeMax == deletion and nodeMax == insertion:      
                backtrack.append(['|','->' ])
            else:
                if nodeMax == insertion:
                    backtrack.append('->')
                elif nodeMax == deletion:
                    backtrack.append('|')
                elif nodeMax == diaganol:
                    backtrack.append('\\')
                else:
                    backtrack.append('*')
                    startBoarder.append((i,j))             
    matrix = []
    for i in range(0, len(backtrack), len(protein2)):
        row = backtrack[i : i+len(protein2)]
        matrix.append(row)
    
    return matrix, nodeDict, maxScore, endBoarder

result = LCS_backtrack_local_allignment(PAM250Matrix, indelPenalty, protein1, protein2)
backtrackMatrix = result[0]
nodeDict = result[1]
maxScore = result[2]
endBoarder = result[3]
print maxScore

outputString1 = ''
outputString2 = '' 
def output_LCS(backtrack, protein1, protein2, i, j):
    global outputString1, outputString2
    if backtrack[i][j] == "*":
        return
    else:
        if backtrack[i][j] == ['|', '->']:
            choice = random.choice(['|', '->'])
        else:
            choice = backtrack[i][j] 
        if choice == '|':
            outputString1 = protein1[i] + outputString1
            outputString2 = '-' + outputString2
            output_LCS(backtrack, protein1, protein2, i-1, j)
        if choice == '->':
            outputString1 = '-' + outputString1
            outputString2 = protein2[j] + outputString2
            output_LCS(backtrack,  protein1, protein2,  i, j-1)
        if choice == '\\':
            outputString1 = protein1[i] + outputString1
            outputString2 = protein2[j] + outputString2
            output_LCS(backtrack, protein1, protein2, i-1, j-1)
#        if choice == 'boarder':
#            outputString1 = '*' + outputString1
#            outputString2 = '*' + outputString2
#            output_LCS(backtrack, protein1, protein2, i-1, j-1)
output_LCS(backtrackMatrix, protein1, protein2, endBoarder[0]-1, endBoarder[1]-1)

print outputString1
print outputString2


