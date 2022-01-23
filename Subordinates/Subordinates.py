from array import array 
from functools import lru_cache
import sys
class Graph: 
    def __init__(self, arr, n):
        self.n=n 
        self.arr=[(j, i+2)  for i, j in enumerate(arr)]
        self.adj=[[] for i in range(n+1)]
        self._create_graph()
        self.counter=[0 for i in range(len(self.arr)+2)]
        self.marked={}

    def _create_graph(self): 
        for i in range(len(self.arr)): 
            self.add(self.arr[i][0], self.arr[i][1])

    def add(self, u, v):
        self.adj[u].append(v)
    

    def dfs(self, source):
        print("currently doing dfs for source {}".format(source))
        self.counter[source]=1 
        self.marked[source]=True
        for v in self.adj[source]:
            if v in self.marked.keys() :
                continue 
            self.dfs(v)
            self.counter[source]+=self.counter[v]

    
            
    
           


def main():
    sys.setrecursionlimit(100)# does not work due to recursion limit set 
    n=int(input())
    arr=array("i", map(int, input().split()))
    graph=Graph(arr, n )
    graph.dfs(1)
    res=[str(i-1) for i in graph.counter][1:]
    print(" ".join(res))


if __name__=='__main__': 
    main() 
