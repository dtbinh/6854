# kleinberg algorithm
# on the k-secretary problem
# input: N, number of candidates, k, number of candidate to select
# W: the list of N-values for each candidate, in the order of arrival.
# output: list of k candidates selected by the algorithm

import math
import numpy

# the optimal algorithm for k = 1
# output: ([the best candidate], [N sampled candidates])
def select_simple(N, W, verbose = False):
    # trivial case when N = 1
    if N == 1:
        candidate = W.pop()
        
        return ([candidate], [candidate])
    
    else:
        l = max(int(N/math.e),1)
        best_sample = W.pop()

        # sampling the L number of candidate
        # list of items
        items = [best_sample]
        for i in range(0,l-1):
            sample = W.pop()
            items.append(sample)
            best_sample = max(best_sample, sample)

        # choosing the one that exceeds the best of the sample
        # from the remaining candidates
        best_candidate = None
        for i in range(0, N-l-1):
            candidate = W.pop()
            items.append(candidate)
            if candidate > best_sample:
                #if best_candidate == None or candidate > best_candidate: 
                if best_candidate == None or candidate > best_candidate: 
                    best_candidate = candidate
                    if verbose: print "Chosen ", candidate

        # if there is no better candidate, use the last one.
        candidate = W.pop()
        items.append(candidate)
        
        if best_candidate == None:
            best_candidate = candidate
            if verbose: print "Chosen ", candidate
            
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
def kleinberg(N, k, W, verbose = False):
    def kleinberg_helper(N, k, W, verbose = False):
        if N < k:
            all_samples = []
            candidates = []
            for i in range (N):
                candidate = W.pop()
                all_samples.append(candidate)
                candidates.append(candidate)
                if verbose: print "Chosen ", candidate

            return (candidates, all_samples)
        
        elif k == 1:
            return select_simple(N, W, verbose)
        else:
            # list of N items sampled in this turn
            all_samples = []
            
            # getting the sample size from binomial distribution
            m = -1
            l = k/2
            while not((m>=l) and (N-m>=(k-l))):
                m = binomial_sample(N, 0.5)

            # choosing k/2 candidate from the samples
            (candidates, samples) = kleinberg_helper(m, l, W, verbose)

            # copy the samples
            all_samples = samples[:]

            # sorting the samples, from smallest to largest
            samples.sort()

            # reverse the samples, now from largest to smallest
            samples.reverse()

            # take the threshold to be the k/2th largest item in the sample
            threshold = samples[l-1]

            # couting the number of candidates have seen
            count = m
            for i in range(N-m):
                candidate = W.pop()
                all_samples.append(candidate)

                if len(candidates) < k:
                    # add to the selected list if this candidate is better than the threshold
                    # or if they are the last few candidates
                    if (candidate>threshold or N-count == k - len(candidates)):
                        candidates.append(candidate)
                        if verbose: print "Chosen ", candidate

                count += 1

            return (candidates, all_samples)
        
    temp = W
    if isinstance(W, list):
        temp = listQueue(W)
    candidates = kleinberg_helper(N, k, temp, verbose)[0]
    
    return candidates

class listQueue(list):
    def __init__(self, L):
        for u in L:
            self.append(u)
            
    def pop(self):
        return list.pop(self, 0)
    
class userInputQueue:
    def __init__(self):
        pass

    def pop(self):
        raw = input("Please enter a value:")
        return float(raw)

Q = userInputQueue()
print Q.pop()

print select_simple(10, listQueue([4,1,3,5,9,0,2,8,6,7]))
# checking if k-kleinberg returns correctly k-items
for i in range(1, 11):
    print kleinberg(10, i, [4,1,3,5,9,0,2,8,6,7])
# interactive version of kleinberg
print kleinberg(10, 3, userInputQueue(), True)
