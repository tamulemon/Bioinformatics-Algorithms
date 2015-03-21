imputList = ''

import re

def generate_list(imputList):
    m = imputList.replace('(', '').replace(')', '')
    output = re.split(r'\s+',m)
    ouputs = map(int, output)
    return ouputs

def find_break_point(imputList):
    seq = generate_list(imputList)
    breakpointNum = 0
    n = len(seq)
    seq.insert(0,0)
    seq.append(n + 1)
    for i in range(len(seq)-1):
        if seq[i+1] != seq[i] + 1:
            breakpointNum += 1
    return breakpointNum

print find_break_point(imputList)