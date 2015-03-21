#protein1 = ''
#protein2 = ''
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
sys.setrecursionlimit(100000)
maxScore = 0

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


def find_midColumn(left, right):
    if (left + right)% 2 == 0:
        midColumn = (left + right) / 2
    else:
        midColumn = int(math.floor((left + right) / 2))
    return midColumn

def LCS_dict_half(top, bottom, left, right):
    nodeDict = {}
    midColumn = find_midColumn(left, right)
    for i in range(top, bottom + 1):
        nodeDict[(i, left)] = indelPenalty * (i - top)
    for j in range(left, midColumn + 2):
        nodeDict[(top, j)] = indelPenalty * (j - left)
    for j in range(left + 1, midColumn + 2):
        for i in range(top + 1, bottom + 1):
            diaganol = nodeDict[(i-1, j-1)] + BLOSUM62Matrix[(protein1[i-1], protein2[j-1])] 
            insertion = nodeDict[(i, j-1)] + indelPenalty
            deletion = nodeDict[(i-1, j)] + indelPenalty
            nodeMax = max(diaganol, insertion, deletion)
            nodeDict[(i,j)] = nodeMax
        for i in range(top, bottom + 1):
            nodeDict.pop((i, j-2), 0)
    return nodeDict
#print LCS_dict_half(0,10,1,6)

def LCS_dict_half_reverse(top, bottom, left, right):
    nodeDict = {} 
    midColumn = find_midColumn(left, right)
    for i in range(bottom, top-1, -1):
        nodeDict[(i, right)] = indelPenalty * (bottom - i)
    for j in range(right, left-1, -1):
        nodeDict[(bottom, j)] = indelPenalty * (right - j)
    for j in range(right-1, midColumn-1, -1):
        for i in range(bottom-1, top-1, -1):
            diaganol = nodeDict[(i+1, j+1)] + BLOSUM62Matrix[(protein1[i], protein2[j])] 
            insertion = nodeDict[(i, j+1)] + indelPenalty
            deletion = nodeDict[(i+1, j)] + indelPenalty
            nodeMax = max(diaganol, insertion, deletion)
            nodeDict[(i,j)] = nodeMax
        for i in range(bottom, top-1, -1):
            nodeDict.pop((i, j+2), 0)
    return nodeDict
#print LCS_dict_half_reverse(0,10,1,6)

def middle_node(top, bottom, left, right):
    nodeDict = LCS_dict_half(top, bottom, left, right)
    point1Score = float('-inf')
    point2Score = float('-inf')
    midColumn = find_midColumn(left, right)
    nextColumn = midColumn + 1
    for i in range(top, bottom + 1):
        score11 = nodeDict[(i, midColumn)] 
        score21 = nodeDict[(i, nextColumn)] 
        if score11 >= point1Score:
            point1Score = score11
            point1 = (i,midColumn)
        if score21 > point2Score:
            point2Score = score21
            point2 = (i,nextColumn)
    return point1, point2, point1Score

maxScore = middle_node(0, len(protein1), 0, len(protein2))[2]
print maxScore

def middle_edge(point1, point2):
    if point1[0] == point2[0] and point1[1] +1 == point2[1]:
        midEdge = '->'
    elif point1[0] + 1 == point2[0] and point1[1] +1 == point2[1]:
        midEdge = '\\'
    else:
        midEdge = '|'
    return midEdge

middleNode = []
def linear_space_alignment(top, bottom, left, right):
    print top, bottom, left, right
    global walkingMap, string1, string2, middleNode
    if bottom <= 0 or right <= 0:
        return
    if top == bottom or left == right:
        middleNode.append((bottom, right))
        return
    else:     
        midPoints = middle_node(top, bottom, left, right)
        midNode = midPoints[0]
        nextNode = midPoints[1]
        print midNode, nextNode 
        middleNode.append(midNode)
        midEdge = middle_edge(midNode,nextNode)
        middle = midNode[1]
        linear_space_alignment(top, midNode[0], left, middle)        
        if midEdge == '->' or midEdge == '\\':
            middle = nextNode[1]
        else:
            middle = midNode[1]
        if midEdge == '|' or midEdge == '\\':
            newTop = midNode[0] + 1
        else:
            newTop = midNode[0]
        linear_space_alignment(newTop, bottom, middle, right) 
linear_space_alignment(0, len(protein1), 0, len(protein2))

middleNode = list(set(middleNode))
middleNode.sort()
print middleNode
string1 = ''
string2 = ''
for i in range(len(middleNode)-1):
    if middleNode[i][0] + 1 == middleNode[i+1][0] and middleNode[i][1] + 1 == middleNode[i+1][1]:
        string1 = string1 + protein1[middleNode[i][0]]
        string2 = string2 + protein2[middleNode[i][1]]
    if middleNode[i][0] + 1 == middleNode[i+1][0] and middleNode[i][1] == middleNode[i+1][1]:   
        string1 = string1 + protein1[middleNode[i][0]]
        string2 = string2 + '-'
    if  middleNode[i][0]  == middleNode[i+1][0] and middleNode[i][1] + 1 == middleNode[i+1][1]:
        string1 = string1 + '-'
        string2 = string2 + protein2[middleNode[i][1]] 
print string1
print string2