# kleinberg algorithm
# on the k-secretary problem
# input: N, number of candidates, k, number of candidate to select
# W: the list of N-values for each candidate, in the order of arrival.
# output: list of k candidates selected by the algorithm

# the optimal algorithm for k = 1
import math
import numpy
def select_simple(N, W):
    if len(W) == 1:
        return (W,W)
    l = max(int(N/math.e),1)
    best_sample = W.pop(0)
    # sampling the L number of candidate
    # list of items
    items = [best_sample]
    for i in range(0,l-1):
        sample = W.pop(0)
        items.append(sample)
        best_sample = max(best_sample, sample)
    # choosing the one that exceeds the best of the sample
    # from the remaining candidates
    best_candidate = None
    for i in range(0, N-l-1):
        candidate = W.pop(0)
        items.append(candidate)
        if candidate > best_sample:
            if best_candidate == None or candidate > best_candidate: 
                best_candidate = candidate
    # if there is no better candidate, use the last one.
    candidate = W.pop(0)
    items.append(candidate)
    if best_candidate == None:
        best_candidate = candidate
    return ([best_candidate], items)

def binomial_sample(N, r, count = 0):
    debug = False
    values = range(N)
    if debug == False:
        return numpy.random.binomial(N, r)
    else:
        if count < N: count += 1
        return values[count-1]
    
# input: N, k, W
# output: (k-size list of candidates, sample population)
def kleinberg(N, k, W):
    def kleinberg_helper(N,k,W):
        if N < k:
            temp = W[:]
            W = []
            return (temp[:], temp[:])
        elif k == 1:
            return select_simple(N, W)
        else:
            temp = W[:]
            # getting the sample size from binomial distribution
            m = binomial_sample(N, 0.5)

            # choosing k/2 candidate from the samples
            (candidates, samples) = kleinberg_helper(m, k/2, W)
            
            # sorting the samples, from smallest to largest
            samples.sort()
            # reverse the samples, now from largest to smallest
            samples.reverse()
            # take the threshold to be the k/2th largest item in the sample
            threshold = samples[k/2]
            
            for i in range(N-m):
                if len(candidates) < k:
                    u = W.pop(0)
                    if (u>threshold):
                        candidates.append(u)

            return (candidates, temp[:N])
    candidates = kleinberg_helper(N, k, W[:])[0]
    return candidates



def kleinberg_will(N,K,W):
    if K == 1:
        return select_simple(N,W)[0]
    
    L = int(math.floor(K/2))
    
    split = binomial_sample(N, .5)
    split = min(split, N - L)
    split = max(split, L)



    rightHalf = W[split:]
    leftHalf = W[:split]
    print '...'
    print split,L,W[:split]
    print '...'
    

    prevAnswers = kleinberg_will(split, L, W[:split])
    
    
    cand = leftHalf
    cand.sort()
    y_L = cand[-L]
    if len(rightHalf) == K-L:
        return prevAnswers + rightHalf
    else:
        chosen = []
        for n in rightHalf:
            if n >= y_L and len(chosen) < K-L:
                chosen.append(n)
        return prevAnswers + chosen
    
        



    
#print select_simple(10, [4,1,3,5,9,0,2,8,6,7])
for x in range(30):
    output = kleinberg_will(10, 5, [4,1,3,5,9,0,2,8,6,7])
    print output
