import re
imputList = ''
def generate_list(imputList):
    m = imputList.replace('(', '').replace(')', '')
    output = re.split(r'\s+',m)
    ouputs = map(int, output)
    return ouputs
#print generate_list(imputList)

def reverse(aList, m, n):
    newList = []
    for i in range(m):
        newList.append(aList[i])
    for j in range(n, m-1, -1):
        newList.append(-aList[j])
    for k in range(n+1, len(aList)):
        newList.append(aList[k])
    return newList

def format_output(aList):
    output = ''
    for x in range(len(aList)):
        if aList[x] > 0:
            output = output + '+' + str(aList[x]) + ' '
        else:
            output = output + str(aList[x])+ ' '
    output = '(' + output + ')'
    return output

seq = generate_list(imputList)    
reversalDistance = 0
def greedy_sorting(seq, k):
    global reversalDistance
    output = ''
    if k == len(seq):
        return
    else:
        intermediate = list(seq)
        if k + 1 != abs(seq[k]):
            if k+1 in seq:
                ind = seq.index(k+1)
            else:
                ind = seq.index(-(k+1))
            intermediate = reverse(seq, k, ind)                    
            output = format_output(intermediate)
            print output
        if k + 1 == -intermediate[k]:
            intermediate[k] = - intermediate[k]
            reversalDistance += 1 
            output = format_output(intermediate)
            print output
        greedy_sorting(intermediate, k+1)

print greedy_sorting(seq, 0)