# kleinberg algorithm
# on the k-secretary problem
# input: N, number of candidates, k, number of candidate to select
# W: the list of N-values for each candidate, in the order of arrival.
# output: list of k candidates selected by the algorithm

# the optimal algorithm for k = 1
import math
import numpy
def select_simple(N, W):
    l = max(int(N/math.e),1)
    best_sample = W.pop(0)
    # sampling the L number of candidate
    for i in range(0,l-1):
        best_sample = max(best_sample, W.pop(0))
    # choosing the one that exceeds the best of the sample
    # from the remaining candidates
    for i in range(0, N-l-1):
        candidate = W.pop(0)
        if candidate > best_sample:
            return candidate
    return W.pop(0)

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
        if k == 1:
            # temporary array for the data
            temp = W[:]
            # sampling population
            samples = W[:N]
            # removing the sample from the queue
            for i in range(N):
                W.pop(0)
            # return chosen value + sample population
            return ([select_simple(N, temp)], samples)
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
    candidates = kleinberg_helper(N, k, W)[0]
    return candidates

    
print select_simple(10, [4,1,3,5,9,0,2,8,6,7])
print kleinberg(10, 3, [4,1,3,5,9,0,2,8,6,7])
