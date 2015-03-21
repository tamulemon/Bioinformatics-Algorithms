#GapOpeningPenalty
sigma = -11
#GapExtentionPenalty
e = -1
protein1 = 'EMHRQWEVKERSCDCTTPDMFSEHFPRSAHWFTKNTVRFKWNFRFHTTTGMEGYMQVHAFFTRSDKTKDSTY'
protein2 = 'EMHRQWMHRTAEYAITPDMFSEHFPRNAHWFTKNTVERWHNPKWGMEGTFSDKTKDSTY'
matrix = '''
   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7
'''
import random
import sys
sys.setrecursionlimit(10000)

def Blosum_62_matrix(matrix):
    lst = list(matrix.split())
    lst.insert(0,' ')
    byRow = []
    BlosumDict = {}
    for i in range(0, len(lst), 21):
        byRow.append(lst[i:i+21])
    for j in range(1, 21):
        for k in range(1, 21):
            BlosumDict[(byRow[0][k], byRow[j][0])] = int(byRow[j][k])
    return BlosumDict
BLOSUM62Matrix = Blosum_62_matrix(matrix)

def alignment_affine_gap_penalties(protein1, protein2):
    lowerDict = {}
    middleDict = {}
    upperDict = {}
    backtrackLower = []
    backtrackMiddle = []
    backtrackUpper = []

    for i in range(len(protein1)+1):
        middleDict[(i,0)] = 0
        upperDict[(i,0)] = 0
    for j in range(len(protein2)+1):
        middleDict[(0,j)] = 0
        lowerDict[(0,j)] = 0
    for i in range(1,len(protein1)+1):
        for j in range(1,len(protein2)+1):
            #
            lowerMax = max(lowerDict[(i-1,j)] + e, middleDict[(i-1,j)] + sigma)
            lowerDict[(i,j)] = lowerMax
            if lowerMax == lowerDict[(i-1,j)] + e and lowerMax != middleDict[(i-1,j)] + sigma:
                backtrackLower.append('|')
            else:
                backtrackLower.append('*')
            #    
            upperMax = max(upperDict[(i,j-1)] + e, middleDict[(i,j-1)] + sigma)
            upperDict[(i,j)] = upperMax
            if upperMax == upperDict[(i,j-1)] + e and upperMax != middleDict[(i,j-1)] + sigma:
                backtrackUpper.append('-')
            else:
                backtrackUpper.append('*')    
            #
            middleMax= max(lowerDict[(i,j)], middleDict[(i-1,j-1)] + BLOSUM62Matrix[(protein1[i-1], protein2[j-1])], upperDict[(i,j)])
            middleDict[(i,j)] = middleMax
            if middleMax == lowerDict[(i,j)]:
                backtrackMiddle.append('*L')
            elif middleMax == upperDict[(i,j)]:
                backtrackMiddle.append('*U')
            else:
                backtrackMiddle.append('\\')          
    maxScore = middleDict[(i,j)] 
    print maxScore
    
    lowerMatrix = []
    middleMatrix = []
    upperMatrix = []
    for i in range(0, len(protein1)*len(protein2), len(protein2)):
        lowerMatrix.append(backtrackLower[i : i+len(protein2)])
        middleMatrix.append(backtrackMiddle[i : i+len(protein2)])
        upperMatrix.append(backtrackUpper[i : i+len(protein2)])

    return  lowerDict,middleDict,upperDict,lowerMatrix, middleMatrix, upperMatrix

result = alignment_affine_gap_penalties(protein1, protein2)
lowerDict = result[0]
middleDict = result[1]
upperDict = result[2]
lowerMatrix = result[3]
middleMatrix = result[4]
upperMatrix = result[5]

outputString1 = ''
outputString2 = '' 
def output_LCS(lowerMatrix, middleMatrix, upperMatrix, protein1, protein2, i, j):
    global outputString1, outputString2
    if i < 0 and j >= 0:
        for x in range(j-i):
            outputString1 = '-' + outputString1
        outputString2 = protein2[0:j-i] + outputString2
        return
    if i >= 0 and j < 0 :
        outputString1 = protein1[0:i-j] + outputString1
        for y in range(i-j):
            outputString2 = '-' + outputString2  
        return
    if i < 0 and j < 0:
        return
    else:
        if middleMatrix[i][j] == '*L':
#            if lowerMatrix[i][j] == '*':
            outputString1 = protein1[i] + outputString1
            outputString2 = '-' + outputString2  
            output_LCS(lowerMatrix, middleMatrix, upperMatrix, protein1, protein2, i-1, j)
        if middleMatrix[i][j] == '*U':
            outputString1 = '-' + outputString1
            outputString2 = protein2[j] + outputString2
            output_LCS(lowerMatrix, middleMatrix, upperMatrix, protein1, protein2, i, j-1)
        if middleMatrix[i][j] == '\\':
            outputString1 = protein1[i] + outputString1
            outputString2 = protein2[j] + outputString2
            output_LCS(lowerMatrix, middleMatrix, upperMatrix, protein1, protein2, i-1, j-1)

output_LCS(lowerMatrix, middleMatrix, upperMatrix, protein1, protein2, len(protein1)-1, len(protein2)-1)

print outputString1
print outputString2

