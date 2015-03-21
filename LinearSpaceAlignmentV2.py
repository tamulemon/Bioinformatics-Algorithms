protein1 = 'PLEASANTLY'
protein2 = 'MEANLY'

indelPenalty = -5
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
import math
import sys
sys.setrecursionlimit(10000)

def string_reverse(string):
    revString = ''
    for i in range(len(string)):
        revString = string[i] + revString
    return revString
protein1Rev = string_reverse(protein1)
protein2Rev = string_reverse(protein2)

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

def LCS_dict(BLOSUM62Matrix, indelPenalty, protein1, protein2):
    nodeDict = {}
    for i in range(len(protein1)+1):
        nodeDict[(i,0)] = indelPenalty * i
    for j in range(len(protein2)+1):
        nodeDict[(0,j)] = indelPenalty * j
    for i in range(1,len(protein1)+1):
        for j in range(1,len(protein2)+1):
            diaganol = nodeDict[(i-1, j-1)] + BLOSUM62Matrix[(protein1[i-1], protein2[j-1])] 
            insertion = nodeDict[(i, j-1)] + indelPenalty
            deletion = nodeDict[(i-1, j)] + indelPenalty
            nodeMax = max(diaganol, insertion, deletion)
            nodeDict[(i,j)] = nodeMax
    return nodeDict
nodeDict = LCS_dict(BLOSUM62Matrix, indelPenalty, protein1, protein2)
nodeDictReverse = LCS_dict(BLOSUM62Matrix, indelPenalty, protein1Rev, protein2Rev)

def middle_node(top, bottom, left, right):
    point1 = []
    point2 = []
    point1Score = float('-inf')
    point2Score = float('-inf')
    if (left + right)% 2 == 0:
        midColumn = (left + right) / 2
        nextColumn = midColumn + 1
    else:
        midColumn = int(math.floor((left + right) / 2))
        nextColumn = int(math.ceil((left + right) / 2))
    for i in range(top, bottom + 1):
        score11 = nodeDict[(i, midColumn)] 
        score12 = nodeDictReverse[(i, right - midColumn)]
        score21 = nodeDict[(i, nextColumn)] 
        score22 = nodeDictReverse[(i, right - nextColumn)]
        sumScore1 = score11 + score12
        sumScore2 = score21 + score22
        if sumScore1 > point1Score:
            point1Score = sumScore1
            point1 = [(i,midColumn)]
        elif sumScore1 == point1Score:
            point1.append((i,midColumn))
        if sumScore2 >point2Score:
            point2Score = sumScore2
            point2 = [(i,nextColumn)]
        elif sumScore2 == point2Score:
            point2.append((i,nextColumn))
        midNode = random.choice(point1)
        nextNode = random.choice(point2)  
    return midNode, nextNode


def middle_edge(point1, point2):
    midEdge = ''
    if point1[0] == point2[0]:
        midEdge = '->'
    elif point1[1] == point2[1]:
        midEdge = '|'
    else:
        midEdge = '\\'
    return midEdge

walkingMap = []
string1 = ''
string2 = ''
def linear_space_alignment(top, bottom, left, right):
    global walkingMap, string1, string2
    print top, bottom, left, right
    if bottom - top <=0 or right - left <= 0:
        return
    else:     
        midPoints = middle_node(top, bottom, left, right)
        midNode = midPoints[0]
        nextNode = midPoints[1]
        middle = midNode[1]
        midEdge = middle_edge(midPoints[0], midPoints[1])
        print midPoints, midEdge
        walkingMap.append(midEdge)
        linear_space_alignment(top, midNode[0], left, middle)        
        if midEdge == '->' or midEdge == '\\':
            middle = midPoints[1][1]
        if midEdge == '|' or midEdge == '\\':
            newMidNode = [None,None]
            newMidNode[0] = midNode[0] + 1
            newMidNode[1] = midNode[1]
            newMidNode = tuple(newMidNode)
            midNode = newMidNode
        linear_space_alignment(midNode[0], bottom, middle, right) 

linear_space_alignment(0, len(protein1), 0, len(protein2))
print walkingMap
