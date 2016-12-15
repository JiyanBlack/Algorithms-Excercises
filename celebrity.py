from random import randrange

length=  1000

G= [[randrange(2) for i in range(length)] for i in range(length)]
c = randrange(length)
for i in range(length):
    G[i][c]=1
    G[c][i]=0

def celebrity(G):
    n=len(G)
    u,v=0,1
    the_celebrity = 0
    # iterate through G, find a possible celebrity
    for i in range(2,n+1):
        if G[u][v]:
            u=i
        else:
            v=i
    # select which is the potential celebrity
    if u==n:
        c = v
    else:
        c = u
    # check if c is the celebrity
    for i in range(n):
        if i==c:
            continue
        if G[c][i] or not G[i][c]:
            break
    else:
        return c
    return None

def celebrity_set(G):
    n=len(G)
    candidates=set(list(range(n)))
    u,v=0,1
    for i in range(2,n+1):
        if G[u][v]:
            candidates.remove(u)
            u=i
        else:
            candidates.remove(v)
            v=i
    return candidates

def celebrity_optimal(G):
    n=len(G)
    celebrity=0
    for i in range(1,n):
        celebrity = i if G[celebrity][i] else celebrity
    return celebrity



print(celebrity(G))
print(celebrity_set(G))
print(celebrity_optimal(G))
