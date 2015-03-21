protein1 = 'WRVMAGEFDFFVHPVWCPEFCQRTVPKLDATEGVILTRNFFKPLRVCFQRVAGGPWHWLMNPDRCFYRFVQQQLMFQDQCDFTGSPHDRDHCDHGTFIVVQKWVVDKIWMTLYIALNWWCVQNEMQADFSTPAPHYILWKSVKLMSNWRNRAEFQVVDHAIYEREQHEVYYDDRTYRIIAREIYFCGTTSQDPVSFNGIHSAAIKYGFTDRISIDMVANQMVKKIPDEQKQCFYKRQCIDGDVLQIGAFHLGEPGNSHQVGGTENNWPGYCSLWVATVLNYKVHREIKSPQFWGSQIKHRSYAQTNINFPRDDSYFSMCYVMPTSQLGIGVDNTFFLIPLECTQKESAMHPCFHKRYLNPSCMKYGPLVDIKGVGDARGWKQYFCTSKWVCTVTEHCMQWFTRANFEKCTGHWFKFHKYWHRPCKCTFYGLHAPYEVIRRRFIGGDTKGHQNSEIPDFALDGYNPDAFGMHDTNGYSLFHAFLDANWVCNQCVALCEQVHYLEQNGMVPGALHWMALAQYVFIKTKHMPPFAAPRNFGGYPGQHTPWLEVAKMQQFVKYVFLRQPAPLIAMYTPECYEGAEIACGVKGVQMNMLVVNCGCWYTMASPCPFKMGIMYINTYMHPHHYQELECHDDGPSYGEYMYVHYLKVPNCYMVSSSDKVCRCHVECSAEPQCHLDIQVLWMKPFHGVHDMYVDYKLHHQIVQGHTTMVQCDQWDHYNKGLDSWCVCPGLDLLQPRQNEEKDTWCSAKRWHWNRDNGGEEFNPEFLGWWNNPQNRSFRILWVMWCRMVQLSGKMRTKNADDIKYKPWKWPKQRLDLEDMGTERMNLICDNYVACEHKFNATPTHHNRDSYKQISTCLNDLMIYMKRVWRVFRRASQWTCTAPKVWSGPMYGVDWMSWPSAKVDGSDGRPHSCTYGWGWKGTGIKKEPGWVEIGEKRINYHTQMHQNWHRVHARDAGVWDQEQWLMPANLPLDYYLDLHLEKEICMMKTRERCKVLQPIKLCHAVFPGHIRQDNPPQYQASFHHWFHNPHVTWLK'
protein2 = 'RVKTSWGIDYNYDGIFDTTWMHIQAWVNILFDYWLCWMKFQPSLVVQLMCSHFPAQAQEQWLICLWQHWKREKGSYVLESSPCGNWSRGNAHPKPAHHSHFFCCHNSTCQGHDFFQMHKSWCHGNECFRITYAMDYRRDLWLAWGMPKDGTWSQNTGPTSIHLFAHHLRNLPVTCCKVRVCTQKPSGASQHTKWLGPFPPQIQDREHVSLWVFKALHCCKWSRHWHPHSHPEKFTMCGRGTQESGFHMTKVLGHQRFLNQLCVEMEAYVIFMKKRFGNTRHHRDGCTYHENKDIHEKQANAYSCMDMFSPFHSNYCRFPQIEETFMFAFNQKHQHHWDTVYMMGMEVPYHKCVYTHPIDTMNYQVCMIEMSKLDYTVKFWMWKEHPIWWYYNLQISCLCMMLFVHHMKHFSDAISDEWAWPMTKPMKTEDFGWYSPTMPHMMTLLCQAHRQNSEIPVFPLEEFDHMTVVGYNPKDTGMCSNYAFGFICHDTNGYSGFHAFLDANWQCNQCVALCEQVHYLEGNGMVAQYVNIKTPYHMPPRNEGGYPVAKMRQFVKYVFLRQPAPLIPECYPGAEIACGQALRQPKQIAVGSPGMSEPHGGCQLDGKCSRFIHCKFIMMCRQTMMCWHTYDPVHMMGTPWSSPFGERCTGDHACWVTNKSNWQCARCDCHGHNSEYSNKSTQYRGVNTVATSDIYFFGSNYVTETNNCCCHQSPIMLNIREDVYKGYLVSRKRELTFYRWNIFADDSRHGMQGPSFDHIYIQMMKISITDNPEAPKRPGIPLRCRTETCVCLIVGHYMASYPMHMICYWENGSVVVGKDAKKRIIHNDMEENPWGYGQIHKDPEIIWDAVLDNHAHWYWKNYNQIENITNFSHTRMQEKDLSNKLPMLPRELNEWMISVNTYFHISYDYVEFPMVFKHTGRHKRSPANCNACDIKHVYTPYMIMTFNYPIIQDYMAKEQKTHSRMPCRCCGNRQKDIKRCDRWSSSLMACSKKVRMPWLVRELAIMYWRPVEFHFMFYQTCRGGYMTNK'
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
  
def LCS_middle_edge_linear_space(BLOSUM62Matrix, indelPenalty, protein1, protein2):
    backtrack = []
    nodeDict = {}
    point1 = ()
    point2 = ()
    maxScore1 = 0
    maxScore2 = 0

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
            if j == len(protein2)/2:
                if nodeMax > maxScore1:
                    maxScore1 = nodeMax
                    point1 = (i,j)
            if j == len(protein2)/2 + 1:
                if nodeMax > maxScore2:
                    maxScore2 = nodeMax
                    point2 = (i,j)     
    return point1, point2

print LCS_middle_edge_linear_space(BLOSUM62Matrix, indelPenalty, protein1, protein2)
