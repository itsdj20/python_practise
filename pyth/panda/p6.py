v = 4
Large = 9999
def fn(G):
    dist = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    s(dist)

def s(dist):
    for i in range(v):
        for j in range(v):
            if(dist[i][j] == Large):
                print("Large")
            else:
                print(dist[i][j],end="")
        print("  ")
        

G = [[2, 5, Large, 8],
         [5, 7, Large, 7],
         [Large, 1, 3, Large],
         [Large, Large, 2, 1]]
fn(G)