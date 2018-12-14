import numpy as np

class Node:

    def __init__(self,name,value,l_child,r_child):
        self.name=name
        self.value=value
        self.l_child=l_child
        self.r_child=r_child

    def __str__(self):
        return str((self.value,(str(self.l_child),str(self.r_child))))

def built_tree(dictionary,d=0):
    if len(dictionary)==0:
        return None
    if len(dictionary)==1:
        return Node(list(dictionary.keys())[0],
            list(dictionary.values())[0],None,None)
    sortedindexes=sorted(list(dictionary.keys()),
        key=(lambda x: dictionary[x][d]))
    print(sortedindexes)
    pivot=sortedindexes[len(sortedindexes)//2]
    lower={i:dictionary[i] for i in sortedindexes[:len(sortedindexes)//2]}
    upper={i:dictionary[i] for i in sortedindexes[len(sortedindexes)//2+1:]}
    return Node(pivot,dictionary[pivot],
        built_tree(lower,(d+1)%len(list(dictionary.values())[0])),
        built_tree(upper,(d+1)%len(list(dictionary.values())[0])))

def find_approx_nearest(tree,value):
    return print("not defined")

def find_exact_nearest(tree,value):
    return print("not defined")

def add_node(tree,value):
    return print("not defined")
