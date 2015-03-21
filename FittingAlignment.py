protein1 = 'CAATCACCCCAATCCCTCAATCCTGGCCCCACGCATAGGCTAATGCCAATCGCGGCCAGGGTATAACCGCCATAACTGTGGGTCAGAAGGGATAAGTTCCACAATCCTATTTTCCTCGAGGCGCTTCGATGCGTTAACGCGTACACTCTGTCGGCCAACCGTGTGGGAGCCGAATTGGCTGGGCTGTTGAACATTCTATCAGTAGATAAACGAAGGTACATCCGAGGTTGTCGATCGACCGCGGGGTCGTAGCGCGTGCATGTTCCTTTCAGGCCCACATACTCCGGAACGGTTCATATCACGACTATTCTTGCACAATCGGACAACGGTGTACCATGGTGGACACCGTAGGAGACCAATACTGCGTAAATCATAAGCATTGGAGAGTGGACTGCTAGCGAGGCTCACCATGGAGTCTCGGTCGGCATCTCCTGACTGCTGTTCCATCGCGTTTTTCTTTTACTCACGCAATAAATCAATACCCCCTAACACAGGCCTGCTCCAGCCTTATTAAGGCCATAGTAGCTCTACATGTAGACCGAACGGAAGCACAGTTTGGTAGAAATTCTTAATCGACTATGGTCCGTGCAGGCCAAAAAAGGAATAATCTTCGAATTCTCACGCCTTCATTAGGGCGCACATGGTGGGGTAAATCACTGCACTCTGTTCGCAGTTAAGCGTTGCAATCAATATCGGCAGAACTCGGAGTCCGTATAAAGCCGCCTCAGCGTGCACACGCCCGTGCGGCACGTCATTAGACGAGGATTCCGGGGGACTGGCCTGTTCGTAATCCACTAAAACAATGGTCCTACCATCTAAAACGCACCGTGTTCCCCTCTACGGGAACCCCCTAGAT'
protein2 = 'AGAGCGCAGAGAAGTCATTAGAACATGTAGCACATCGCTTATTAAGGGTCAATACCTAAAGGGCCTAACTATACGCCACACGGAACAGCTC'
indelPenalty = -1
mismatchPenalty = -1

import random
import sys
sys.setrecursionlimit(10000)

def LCS_fitting_alignment(protein1, protein2):
    nodeDict = {}
    backtrack = []
    outputString = ''
    maxScore = 0
    endBoarder = ''
    for i in range(len(protein1)+1):
        nodeDict[(i,0)] = 0
    for j in range(len(protein2)+1):
        nodeDict[(0,j)] = indelPenalty * j 
    for i in range(1,len(protein1)+1):
        for j in range(1,len(protein2)+1):
            if protein1[i-1] == protein2[j-1]:
                diaganol = nodeDict[(i-1, j-1)] + 1
            else:
                diaganol = nodeDict[(i-1, j-1)] + mismatchPenalty  
            deletion = nodeDict[(i-1,j)] + indelPenalty
            insertion = nodeDict[(i,j-1)] + indelPenalty
            nodeMax = max(deletion, insertion, diaganol)
            nodeDict[(i,j)] = nodeMax
            if nodeMax > maxScore and j == len(protein2):
                maxScore = nodeMax
                endBoarder = (i,j)
            if nodeMax == deletion and nodeMax == insertion:      
                backtrack.append(['|','->' ])
            else:
                if nodeMax == insertion:
                    backtrack.append('->')
                elif nodeMax == deletion:
                    backtrack.append('|')
                else:
                    backtrack.append('\\')                          
    matrix = []
    for i in range(0, len(backtrack), len(protein2)):
        row = backtrack[i : i+len(protein2)]
        matrix.append(row)
    return matrix, nodeDict, maxScore, endBoarder

result = LCS_fitting_alignment(protein1, protein2)
backtrackMatrix = result[0]
nodeDict = result[1]
maxScore = result[2]
endBoarder = result[3]
print maxScore

outputString1 = ''
outputString2 = '' 
def output_LCS(backtrack, protein1, protein2, i, j):
    global outputString1, outputString2
    if i < 0 or j < 0:
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

output_LCS(backtrackMatrix, protein1, protein2, endBoarder[0]-1, endBoarder[1]-1)

print outputString1
print outputString2


