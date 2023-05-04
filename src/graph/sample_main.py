from queue import Queue
from dfs import *

def main_dfs():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
    for i in range(n):
         g[i].sort()

    seen = [False] * n
    v = 0
    dfs(g, v, seen)    

if __name__ == "__main__":
    # Change main function to be called as needed.
    main_dfs()