seq1 = 'AGATAGAT'
seq2 = 'CCGCTTGA'
seq3 = 'CTGTCATT'

indelPenalty = -0.0001
### becaue I introduced a very small penalty for indel to incurage mismatch, the final score need to be rounded to integer
import sys
sys.setrecursionlimit(10000)

def LCS_multiple_alignment(seq1, seq2, seq3):
    string1 = ''
    string2 = ''
    string3 = ''
    nodeDict = {}
    maxScore = float('-inf')
    for i in range(0, len(seq1)+1):
        for j in range(0, len(seq2)+1):
            for k in range(0, len(seq3)+1):
                if k == 0 or j == 0 or i == 0:
                    nodeDict[(i,j,k)] = [0,'stop']
                else:
                    if seq1[i-1] == seq2[j-1] == seq3[k-1]:
                        matchScore = 1
                    else:
                        matchScore = 0
                    s1 = nodeDict[(i-1,j,k)][0] + indelPenalty*2
                    s2 =  nodeDict[(i,j-1,k)][0] + indelPenalty*2
                    s3 =  nodeDict[(i,j,k-1)][0] + indelPenalty*2
                    s4 =  nodeDict[(i-1,j-1,k)][0] + indelPenalty
                    s5 =  nodeDict[(i-1,j,k-1)][0] + indelPenalty
                    s6 =  nodeDict[(i,j-1,k-1)][0] + indelPenalty
                    s7 =  nodeDict[(i-1,j-1,k-1)][0] + matchScore
                    maxScoreNode = max(s1,s2,s3,s4,s5,s6,s7)
                    nodeDict[(i,j,k)] = [maxScoreNode,None]
                    if maxScoreNode > maxScore:
                        maxScore = maxScoreNode
                    if maxScoreNode == s1:          
                        nodeDict[(i,j,k)] = [maxScoreNode,'*--']
                    elif maxScoreNode == s2:
                        nodeDict[(i,j,k)] = [maxScoreNode,'-*-']
                    elif maxScoreNode  == s3:
                        nodeDict[(i,j,k)] = [maxScoreNode,'--*']
                    elif maxScoreNode == s4: 
                        nodeDict[(i,j,k)] = [maxScoreNode,'**-']
                    elif maxScoreNode == s5: 
                        nodeDict[(i,j,k)] = [maxScoreNode,'*-*']
                    elif maxScoreNode == s6:
                        nodeDict[(i,j,k)] = [maxScoreNode,'-**']
                    else:
                        nodeDict[(i,j,k)] = [maxScoreNode,'***']                   
    print maxScore
### becaue I introduced a very small penalty for indel to incurage mismatch, the final score need to be rounded to integer
    return nodeDict

string1 = ''
string2 = ''
string3 = ''
nodeDict = LCS_multiple_alignment(seq1, seq2, seq3)
def LCS_multiple_traceback(i,j,k):
    global string1, string2, string3
    if i == 0 and j != 0 and k != 0:
        for x in range(j-1, -1, -1):
            string2 = seq2[x] + string2
        for y in range(k-1, -1, -1):
            string3 = seq3[y] + string3
        return
    if i != 0 and j == 0 and k != 0:
        for x in range(i-1, -1, -1):
            string1 = seq1[x] + string1
        for y in range(k-1, -1, -1):
            string3 = seq3[y] + string3
        return
    if i != 0 and j != 0 and k == 0:
        for x in range(i-1, -1, -1):
            string1 = seq1[x] + string1
        for y in range(j-1, -1, -1):
            string2 = seq2[y] + string2
        return  
    else:
        if nodeDict[(i,j,k)][1] == '*--':
            string1 = seq1[i-1] + string1 
            string2 = '-' + string2 
            string3 = '-' + string3 
            LCS_multiple_traceback(i-1,j,k)
        elif nodeDict[(i,j,k)][1] == '-*-':
            string1 = '-' + string1
            string2 = seq2[j-1]  + string2 
            string3 = '-' + string3  
            LCS_multiple_traceback(i,j-1,k)
        elif nodeDict[(i,j,k)][1] == '--*':
            string1 = '-' + string1
            string2 = '-' + string2
            string3 = seq3[k-1] + string3
            LCS_multiple_traceback(i,j,k-1)
        elif nodeDict[(i,j,k)][1] == '**-':
            string1 = seq1[i-1] + string1 
            string2 = seq2[j-1] + string2 
            string3 = '-' + string3  
            LCS_multiple_traceback(i-1,j-1,k)
        elif nodeDict[(i,j,k)][1] == '*-*':
            string1 = seq1[i-1] + string1
            string2 = '-' + string2
            string3 = seq3[k-1] + string3
            LCS_multiple_traceback(i-1,j,k-1)
        elif nodeDict[(i,j,k)][1] == '-**':
            string1 = '-' + string1
            string2 = seq2[j-1]  + string2 
            string3 = seq3[k-1] + string3
            LCS_multiple_traceback(i,j-1,k-1)
        else:
            string1 = seq1[i-1] + string1
            string2 = seq2[j-1] + string2 
            string3 = seq3[k-1] + string3
            LCS_multiple_traceback(i-1,j-1,k-1)
        return
LCS_multiple_traceback(len(seq1),len(seq2),len(seq3)) 
maxlen = max(len(string1), len(string2), len(string2))
if len(string1) < maxlen:
    for i in range(maxlen - len(string1)):
        string1 = '-' + string1
if len(string2) < maxlen:
    for i in range(maxlen - len(string2)):
        string2 = '-' + string2
if len(string3) < maxlen:
    for i in range(maxlen - len(string3)):
        string3 = '-' + string3
print string1 
print string2 
print string3 