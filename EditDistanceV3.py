protein1 = 'YTMPEMVFHLEGHQGKMSLACWRLECMRVGGYEFVKWWMTCHSMVWNWKFYYFCGMYLWTGKTDIMYRCKPSLVPVHHYPYTNVQEMRSRWSIWTNKRTARLKGGYEELHEAICGSPTPYQERNHVENTYPHVEQYDDCYNQCYVVVFKINHLRATYTSEMSRGVQLFCMRYQMSYMMKMKTDHKWVTAPGMLFWHYMCHCVRKPRYQGHCCRMIKWCIKECLANDCYAYDAAEPCPLVDKKRSGTNEMWVHFVAKNMMVEPKLEYRVEFGAFLFCLNSSRQNGTIFLWKDSAHDTHPDDMTSRQWESWWDRQQANYVDLTVQHDGRDDVNDTERSWEFLVWHCFMLQATWSHKMRKYCDNNAHEANDLLGGPVVCVITVNPERKMWRKSHESSPIRQAKMARQGSERWECKNCWCATWHMYTAEIGDTKFIETLNCLKLENQNMMRGHLLLLCCAMEPFGWVNRKSKHQPSDKCRHLKRGRMKTSFNYTDCWQTMWSQPIKHELKIRSYQSGNPQFKAPNNGRYSDVFSACAMPHQSALADYKKRHMDAWQWNDVQVNANKVYDLKYTCGHIHWDKFTHCNSARLAVKHHNKHCGYVMDNMILETDVRNWAGIEMMDMQDLFESRMPSQNGFEFTPWQLGAGQTLHSNHFANATFRLKTTRIVDSILMALVSNNVWNDNYFGHSIWTEAPMTDERQTCGIFMESIGDDHIIAIQLPCDRLGSFQLANPVIQFTCPDRQNPKKAVWKWNAQMGIRKQRRFNPVKMHPPTVCICGKSEVKPFGP'
protein2 = 'YTMPYKDANHTMVSHDYYGQKEGTQGKEHSIQTWWRHWHEYHTNVECMGDKGPCKQHVGGYEFVYKWWMTCHSMVSLQNWKFYYFCGMYLWTGKTDIANVYFYGDYKKFWCCVVLCKRSAVPMHHYPQWVSVTNVQEMRSRWSIWTNKRTAENDWDKGGYEELHMAICGSPTNYQERNHVPSRANAEYRYRNQCYFKINHLRATYTWEMSRFCMRYNMSYKMPMKTGMLFWHYMCHKASRPQGHECRMIKWCIKECLANDCYAYDPLVDKKRSGTNEMWVHFVAKNMFFEEPKLRGRTMWMQALRNQGYTFEFGACWNANRQNGTIFLHKDHFPAFTHDTHPDDMTSRQWESWNHWTQPIWDERQQANYFDLTVQHDGRDDVNDTERSVEDKTDHLLSLCFMLQMTWSHKVRKYHEANWLLGGPVVCVITVNPERKMWRPARQAKMARQGSECKNCWCATWHMYTAKIGDTERISTLNIILETMMRGHLLLLMYGIECAMEPFGKQPSDKCMHLKREFSFEKMSFNYTDCWPTMWSQPIKHELCIRSYQSGNLQCAAMKKVCGRYSDRFSACAMPHQSALADYKKRHMQAWRWNDVQVNAPYKLCMLENKCMDLKAIWIGWSKSHCGHICNSARRACRQVKHHEMNAMGPIDNWAGIEKMDMQDSFEPRCPSQNGFEFTPWQLVKAIQQAFGQTLHSNHFKIILNATFRLKTTRIVSTLHNADISIGIMLFKFYFNVWNDNYFGHSIWTEKTFNEMHNFIEYCNVQEFNDGDDHFIAMWRHLFLDRLGSFQLANPFHLGAPPCTTSCTDRQNPKKAVGIRKAGRRNNPVKMHVPTMCICGHTSTSELSEVKPQGP'
#protein1 = 'PLEASANTLY'
#protein2 = 'MEANLY'
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
                diaganol = nodeDict[(i-1, j-1)] + 0.5
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

backtrackMatrix = LCS_backtrack(protein1, protein2)[0]
nodeDict = LCS_backtrack(protein1, protein2)[1]

outputString1 = ''
outputString2 = '' 
editDistance = 0
def output_LCS(backtrack, protein1, protein2, i, j):
    global outputString1, outputString2, editDistance
    if i < 0 and j >= 0:
        for x in range(j-i):
            outputString1 = '-' + outputString1
            editDistance -= 1
        outputString2 = protein2[0:j-i] + outputString2
        return
    if i >= 0 and j < 0 :
        outputString1 = protein1[0:i-j] + outputString1
        for y in range(i-j):
            outputString2 = '-' + outputString2 
            editDistance -= 1
        return
    if i < 0 and j < 0:
        return
    else:
        if backtrack[i][j] == ['|', '->']:
            choice = random.choice(['|', '->'])
        else:
            choice = backtrack[i][j] 
        if choice == '|':
            outputString1 = protein1[i] + outputString1
            outputString2 = '-' + outputString2
            editDistance -= 1
            output_LCS(backtrack, protein1, protein2, i-1, j)
        if choice == '->':
            outputString1 = '-' + outputString1
            outputString2 = protein2[j] + outputString2
            editDistance -= 1
            output_LCS(backtrack,  protein1, protein2,  i, j-1)
        if choice == '\\':
            outputString1 = protein1[i] + outputString1
            outputString2 = protein2[j] + outputString2
            if protein1[i] != protein2[j]:
                editDistance -= 1
            output_LCS(backtrack, protein1, protein2, i-1, j-1)

output_LCS(backtrackMatrix, protein1, protein2, len(protein1)-1, len(protein2)-1)

print editDistance