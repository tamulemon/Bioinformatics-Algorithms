k = 3
s1= 'TCTTGCAGCTCGTCA'
s2 = 'GTACTTTCAGAATCA' 
def rev_com(s):
    rev_com_s = str()
    rev_com_dict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    for i in range(len(s)):
        rev_com_s = rev_com_dict[s[i]] + rev_com_s
    return rev_com_s

def get_revcom_kmer_pos(seq, k):
    StrPos = {}
    i = 0
    for i in range(len(seq)-k+1):
        string = seq[i:i+k]
        RVString = rev_com(string)
        if StrPos.has_key(string) == False:
            StrPos[string] = [i]
        else:
            StrPos[string].append(i)
        if StrPos.has_key(RVString) == False:
            StrPos[RVString] = [i]
        else:
            StrPos[RVString].append(i)
    return StrPos

def shared_kmers(k, s1, s2):
    sharedKmerPos = []
    s2Dict = get_revcom_kmer_pos(s2, k)
    for i in range(len(s1)-k+1):
        string1 = s1[i:i+k]
        pos2 = s2Dict.get(string1)
        if pos2 != None:
            for x in pos2:
                sharedKmerPos.append((i,x))
#    sharedKmerPos.sort()
    return sharedKmerPos  
print shared_kmers(k, s1, s2)
