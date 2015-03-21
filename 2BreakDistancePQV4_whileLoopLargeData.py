seq1 = ''
seq2 = ''

import re

# from oriented blocks to list of nodes
def chromosome_to_cycle(seq):
    cycle = []
    for i in range(len(seq)):
        if seq[i] > 0:
            cycle.append(2*seq[i] -1)
            cycle.append(2*seq[i])
        if seq[i] < 0:
            cycle.append(-2*seq[i])
            cycle.append(-2*seq[i]-1)
    return cycle


# parse out each chromosome from parentheses
def generate_chrom_list(chromosomes):
    # some re operations. 
    x = re.findall(r'\((.*?)\)',chromosomes)
    y = []
    for i in x:
        chrom = map(int, re.split(r'\s+', i))
        y.append(chrom)
    return y

# from a list of chromosomes(raw in parentheses), to tuple of nodes denoting colored edges
# "non blocks"
def colored_edges(chromosomes):
    edges = []
    chromList = generate_chrom_list(chromosomes)
    for chrom in chromList:
        nodes = chromosome_to_cycle(chrom)
        circleNodes = nodes + nodes
        for i in range(0, len(nodes), 2):
            edges.append((circleNodes[i+1],circleNodes[i+2]))
    return edges


colorP =  colored_edges(seq1)
colorQ =  colored_edges(seq2)
blockNum = len(colorP)
#print colorP
#print colorQ
workingP = colored_edges(seq1)
workingQ = colored_edges(seq2)
cycles = []
cycleP = []
cycleQ = []
nodesP = []
nodesQ = []
            
def construct_alternating_cycle(nodes, P, Q):
    global cycles, cycleP, cycleQ, nodesP, nodesQ
    while True:
        if P == [] or Q == []:
            return
        else:
            for node in nodes:
                for edgeP in P:
                    if node in edgeP and edgeP not in cycleP:
                        cycleP.append(edgeP)
                        nodesP.extend(edgeP)
                for edgeQ in Q:
                    if node in edgeQ and edgeQ not in cycleQ:
                        cycleQ.append(edgeQ)
                        nodesQ.extend(edgeQ)
            remainingNodes = set(nodesP).symmetric_difference(nodesQ)
            if remainingNodes == set([]):
                cycles.append(cycleP + cycleQ)
                for x in cycleP:
                    workingP.remove(x)
                for y in cycleQ:
                    workingQ.remove(y)
                cycleP = []
                cycleQ = []
                nodesP = []
                nodesQ = []
                if workingP == [] or workingQ == []:
                    return
                else:
                    nodes = workingP[0]
                    P = workingP
                    Q = workingQ  
            else:
                nodes = remainingNodes
                P = workingP
                Q = workingQ  
            
construct_alternating_cycle(colorP[0], colorP, colorQ)    

cyclePQNum = len(cycles)
distance = blockNum - cyclePQNum
print distance
