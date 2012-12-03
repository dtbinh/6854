
def permute(W):

    def permute_helper(W, i):
        if i == len(W)-1:
            yield W[:]
        else:
            for j in range(i, len(W)):
                (W[i], W[j]) = (W[j], W[i])
                S = permute_helper(W, i+1)
                for u in S:
                    yield u
                (W[i], W[j]) = (W[j], W[i])
    S = permute_helper(W, 0)
    while (True):
        yield S.next()

permute([0, 1, 2, 3])
S = permute([0,1,2,3])

for u in S:
    print u

##class permutor:
##    def __init__(self, W):
##        self.W = W
##        self.stack = []
##        for i in range(0, len(W)-1):
##            self.stack.append((i,i))
##    def permute(self):
##        W = self.W
##        while (True):
##            (i,j) = self.stack.pop(0)
##            if (j<len(W)):
##                (W[i], W[j]) = (W[j], W[i])
##                if (i<j and j < len(W)-1):
##                    self.stack.insert(0, (j, i)) 
##                    self.stack.insert(0, (i, j+1))
##                    for i in range(i+1, len(W)-1):
##                        self.stack.insert(0, (i, i))
##                    return W
##        
##
##p = permutor([0, 1, 2, 3])
##while (True):
##    print p.permute()
