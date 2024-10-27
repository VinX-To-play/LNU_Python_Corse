lst = [1,2,3,4,6,6]

def n_pair(lst):
    nPair = 0
    for i in range(len(lst - 1)):
        if lst[i] == lst[i + 1]:
            nPair += 1
    return nPair

def one_pair(lst):
    
            

one_pair(lst)