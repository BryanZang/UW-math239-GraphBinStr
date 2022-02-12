##
##=======================================================
## Bryan Zang (20897536)
## MATH239 Winter 2022
## Tutorial 06, Question 2
##=======================================================
##


def bin_str(n):
    '''
    consumes an integer n and returns a list of binary strings
    that have at most one block of 1's
    
    bin_str: int -> (listof str)
    
    Requires:
      n is non-negative integer
    
    Examples:
      bin_str(0) => ['']
      bin_str(2) => ['00', '01', '10', '11']
    '''
    # create lst of bin str of n bits
    L = []
    for i in range(2**n, 2**(n+1)):
        L.append(bin(i)[3:])
    
    # remove str that has more than one block of 1's
    for j in L:
        if '101' in j:
            L.remove(j)
    
    return L


def xor(L):
    '''
    consumes a list of binary strings and returns a dictionary of
    the amount of vertices and edges it has when converted into a graph
    
    xor: (listof Str) -> (dictof Str:int)
    
    Requires:
      L must be a list of binary strings
      
    Examples:
      xor(['']) => {'vertices': 0, 'edges': 0}
      xor(['00', '01', '10', '11']) => {'vertices': 4, 'edges': 4}
    '''
    if L == ['']: # compensate for empty set
        return {'vertices': 0, 'edges': 0}
    
    # convert binary strings to integers
    for i in range(len(L)):
        L[i] = int(L[i], 2)
    
    # create list of all pair combinations
    N = [(L[i],L[j]) for i in range(len(L)) for j in range(i+1, len(L))]
    
    # append # of 1's in xor result of each pair combination
    M = [] 
    for i in N:
        # str1 xor str2 => existence of edge when result bit is 1
        M.append(bin(i[0] ^ i[1])[2:].count('1'))
    
    return {'vertices': len(L), 'edges': M.count(1)}


def total_str_set(n):
    '''
    consumes an integer n and returns a dictionary depicting amount of
    graph vertices and edges per each integer i=0...n
    
    total_str_set: int -> (dictof Str:(dictof Str:int))
    
    Requires:
      n must be a non-negative integer
    
    Examples:
      total_str_set(0) => {'n=0': {'vertices': 0, 'edges': 0}}
      total_str_set(1) => {'n=0': {'vertices': 0, 'edges': 0},
                           'n=1': {'vertices': 2, 'edges': 1}}
      total_str_set(2) => {'n=0': {'vertices': 0, 'edges': 0},
                           'n=1': {'vertices': 2, 'edges': 1},
                           'n=2': {'vertices': 4, 'edges': 4}}
    '''
    # append dict of # of vertices and # of edges
    L = {}
    for i in range(n+1):
        L['n='+str(i)]=(xor(bin_str(i)))
    return L