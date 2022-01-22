from array import array 

class Tree:
    class Node: 
        def __init__(self, val):
            self.val=val
            self.children=[]
        def add_children(self, node): 
            self.children.append(node)
            return 

    def __init__(self,arr): 
        self.map={}
        self.arr=[(j, i+2 ) for i , j in enumerate(arr)]
        self.root=self.Node(1)
        self.map[1]=self.root
        self._construct_map()
        self.children_count={}
    
    def _construct_map(self): 
        for i in range(len(self.arr)): 
            parent, child=self.arr[i]
            parent_node, child_node=None, None
            if parent not in self.map.keys(): 
                parent_node=self.Node(parent)
                self.map[parent]=parent_node
            else: 
                parent_node=self.map[parent]
            
            if child not in self.map.keys(): 
                child_node=self.Node(child)
                self.map[child]=child_node
            else: 
                child_node=self.map[child]
            parent_node.add_children(child_node)


        
    def find_children(self, node):
        if node not in self.map.keys(): 
            return 0
        if len(self.map[node].children)==0: 
            return 0 

        if node in self.children_count.keys(): 
            return self.children_count[node]
        
        res=len(self.map[node].children)
        for child in self.map[node].children: 
            res+=self.find_children(child.val)
        
        self.children_count[node]=res
        return res
            



           


def main():
    n=int(input())
    arr=array("i", map(int, input().split()))
    tree=Tree(arr)
    res=[]
    for i in range(1, n+1): 
        res.append(tree.find_children(i))
    res=[str(i) for i in res]
    print(" ".join(res))



if __name__=='__main__': 
    main() 
