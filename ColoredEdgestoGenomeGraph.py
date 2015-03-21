imputList = '(+1 -2 -3 +4)'
import re

def generate_list(imputList):
    m = imputList.replace('(', '').replace(')', '')
    output = re.split(r'\s+',m)
    ouputs = map(int, output)
    return ouputs

def chromosome_to_cycle(seq):
#    seq = generate_list(imputList)
    cycle = []
    for i in range(len(seq)):
        if seq[i] > 0:
            cycle.append(2*seq[i] -1)
            cycle.append(2*seq[i])
        if seq[i] < 0:
            cycle.append(-2*seq[i])
            cycle.append(-2*seq[i]-1)
    return cycle

def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(0, len(cycle), 2):
        if cycle[i+1] > cycle[i]:
            chromosome.append(cycle[i+1]/2)
        if cycle[i+1] < cycle[i]:
            chromosome.append(-cycle[i]/2)
            
    return chromosome
        
chromosomes = '(+1 -2 -3)(+4 +5 -6)'
def generate_chrom_list(chromosomes):
    # some re operations. 
    m = chromosomes[chromosomes.find("(")+1:chromosomes.find(")")]
    n = re.match(r'\((.*?)\)', chromosomes).group(1)
    
    x = re.findall(r'\((.*?)\)',chromosomes)
    y = []
    for i in x:
        chrom = map(int, re.split(r'\s+', i))
        y.append(chrom)
    return y

def colored_edges(chromosomes):
    edges = []
    chromList = generate_chrom_list(chromosomes)
    for chrom in chromList:
        nodes = chromosome_to_cycle(chrom)
        circleNodes = nodes + nodes
        for i in range(0, len(nodes), 2):
            edges.append((circleNodes[i+1],circleNodes[i+2]))
    return edges

genomeGraph = [(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)]

def color_edge_to_chrom(colorEdges):
    blackEdges = []
    for i in colorEdges:
        if i[1] - i[0] == 3:
            blackEdges.extend([(i[0]+1, i[0]), (i[1], i[1]-1)])           
        elif i[1] - i[0] == 2:
            if i[0]%2 == 0:
                blackEdges.extend([(i[0]-1, i[0]), (i[1], i[1]-1)])
            if i[0]%2 == 1:
                blackEdges.extend([(i[0]+1, i[0]), (i[1], i[1]+1)])
        elif i[1] - i[0] == 1:
                blackEdges.extend([(i[0]-1, i[0]), (i[1], i[1]+1)])
    blackEdges = list(set(blackEdges))
    outputEdges = []
    for i in blackEdges:
        for j in range(len(i)):
            outputEdges.append(i[j]) 
    chromosome = cycle_to_chromosome(outputEdges)
    return chromosome

def format_output(aList):
    output = ''
    for x in range(len(aList)):
        if aList[x] > 0:
            output = output + '+' + str(aList[x]) + ' '
        else:
            output = output + str(aList[x])+ ' '
    output = '(' + output + ')'
    return output

def graph_to_genome(genomeGraph):
    cycles = []
    cycleBreak1 = 0
    chromosomes = []
    for x in range(len(genomeGraph)):
        if genomeGraph[x][1] - genomeGraph[x][0] <0:
            cycleBreak2 = x
            cycles.append(genomeGraph[cycleBreak1:cycleBreak2])
            cycleBreak1 = cycleBreak2
    for i in cycles:
        chrom = color_edge_to_chrom(i)
        output = format_output(chrom)
        chromosomes.append(output)
        
    return chromosomes

print graph_to_genome(genomeGraph)