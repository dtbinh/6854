from kleinberg import kleinberg
import numpy.random

def random_kleinberg_test():
    print 'Beginning Test....'
    print ''




# Returns the best possible result of the kleinberg algorithm 
def bestPossible(seq,k):
    sSeq = seq
    sSeq.sort()
    return sSeq[len(sSeq)-k:]

# Generates length-arrays of numbers drawn from distribution 
def distributionList(distribution, length):
    out = []
    for i in range(length):
        out.append(distribution())
    return out

# Returns an array of tuples containing the selected
# elements and the competitive ratio
def testSeq(seq,k,times):
    opt = bestPOssible(seq,k)
    out = []
    for i in range(times):
        cur = kleinberg(seq, len(seq), k)
        outTup = (cur, float(sum(cur))/sum(opt)) # (K selected elements, comp-ratio)
        out.append(outTup)
    return out
        
