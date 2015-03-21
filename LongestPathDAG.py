startNode = 4
sinkNode = 41
weightedEdge = '''
34->40:9
17->26:7
13->19:6
6->26:37
16->25:11
37->39:6
20->30:2
14->21:28
1->41:31
11->30:36
9->25:31
14->41:5
7->26:4
33->41:4
33->40:10
3->45:3
5->24:6
3->20:12
5->21:35
39->45:3
7->28:7
8->15:30
40->41:13
18->32:15
20->26:38
22->26:14
30->41:15
18->40:0
4->38:16
13->26:33
14->35:12
30->37:39
13->43:6
21->44:10
9->15:25
1->4:0
22->32:39
30->45:38
2->6:30
19->31:35
5->30:32
0->45:38
19->34:23
1->5:33
8->9:37
2->27:35
27->39:32
15->33:10
10->23:21
3->36:36
4->20:10
2->31:1
5->6:29
20->33:39
4->26:26
18->21:26
36->40:3
23->28:7
31->40:35
17->34:0
7->44:9
'''
import re
import random
#import sys
#sys.setrecursionlimit(10000)

def generate_weighted_edge(weightedEdge):
    weightedEdges = {}
    allNodes = []
    formatted = re.findall(r"[\w']+", weightedEdge)
    for i in range(0, len(formatted),3):
        startNode = int(formatted[i])
        endNode = int(formatted[i+1])
        weight = int(formatted[i+2])
        weightedEdges[(startNode, endNode)] = weight
        allNodes.extend([startNode, endNode])
    allNodes = list(set(allNodes))
    allNodes.sort
    return allNodes, weightedEdges 

def longest_path_DAG(startNode, sinkNode, weightedEdge):
    allNodes = generate_weighted_edge(weightedEdge)[0]
    edgeWeights = generate_weighted_edge(weightedEdge)[1]
    nodeValueDict = {(startNode):0}
    walkingDirection = []
    for a_node in allNodes:
        precursor = []
        maxNodeValue = 0
        for key, value in edgeWeights.items(): 
            if key[1] == a_node:
                if nodeValueDict.has_key(key[0]):
                    nodeValue = nodeValueDict[key[0]] + value
                    if nodeValue >= maxNodeValue:
                        maxNodeValue = nodeValue
                        precursor .append(key[0])
        if maxNodeValue != 0:
            nodeValueDict[a_node] = maxNodeValue
            walkingDirection.append([precursor, a_node])
    output = ''
    trackNode = sinkNode
    while True:
        output = str(trackNode) + '->' + output
        if trackNode == startNode:
            break
        else:    
            for edge in walkingDirection:
                if edge[1] == trackNode:
                    trackNode = random.choice(edge[0])
    return nodeValueDict[sinkNode],output

print longest_path_DAG(startNode, sinkNode, weightedEdge)