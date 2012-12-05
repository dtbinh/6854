from kleinberg import kleinberg
import numpy.random

def random_kleinberg_test(distributionFunct, length, k, numTests, timesPerTest):
    print 'Beginning Test....'
    print 'Generating ' + str(numTests) + ' random ' + str(length) + ' length sequences...'
    testSeqs = [distributionRandom(length, distributionFunct) for i in range(numTests)]
    print 'Running Kleinberg algorithm...'
    testSolutions = [testSeq(seq, k, timesPerTest) for seq in testSeqs]
    return testSolutions

def aveCompRatioOfTest(testSolutions):
    ratios = [sol[1] for sol in testSolutions]
    aveRatio = sum(ratios)/len(ratios)
    return aveRatio

# Returns the best possible result of the kleinberg algorithm 
def bestPossible(seq,k):
    sSeq = seq
    sSeq.sort()
    return sSeq[len(sSeq)-k:]


# Returns randomly permuted length-length array of function
# called on all ints between 0 and length 
def distributionRandom(length, function):
    a = [function(i) for i in range(length)]
    return numpy.random.permutation(a).tolist()

# Calls function on each value in values
def distributionFixed(values, function):
    a = [function(i) for i in values]
    return a


# Returns an array of tuples containing the selected
# elements and the competitive ratio and the average
# competitive ratio
def testSeq(seq,k,times):
    opt = bestPossible(seq,k)
    out = []
    totComp = 0
    for i in range(times):
        cur = kleinberg(len(seq), k, seq)
        comp = float(sum(cur))/sum(opt)
        totComp += comp
        outTup = (cur, comp) # (K selected elements, comp-ratio)
        out.append(outTup)
    totComp /= times
    return out,totComp
        
f = lambda x:x**3
a = random_kleinberg_test(f, 1000, 100, 10, 10)
