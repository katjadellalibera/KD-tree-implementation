import numpy as np
import random as random

class Node:

    def __init__(self,name,value,l_child,r_child,d):
        self.name=name
        self.value=value
        self.l_child=l_child
        self.r_child=r_child
        self.d=d

    def __str__(self):
        return str((self.name,(str(self.l_child),str(self.r_child))))
    #def __str__(self):
    #    return str(self.name)

def build_tree(dictionary,d=0):
    if len(dictionary)==0:
        return None
    if len(dictionary)==1:
        return Node(list(dictionary.keys())[0],
            list(dictionary.values())[0],None,None,d)
    sortedindexes=sorted(list(dictionary.keys()),
        key=(lambda x: dictionary[x][d]))
    pivot=sortedindexes[len(sortedindexes)//2]
    lower={i:dictionary[i] for i in sortedindexes[:len(sortedindexes)//2]}
    upper={i:dictionary[i] for i in sortedindexes[len(sortedindexes)//2+1:]}
    return Node(pivot,dictionary[pivot],
        build_tree(lower,(d+1)%len(list(dictionary.values())[0])),
        build_tree(upper,(d+1)%len(list(dictionary.values())[0])),d)

def find_approx_nearest(tree,value):
    if tree.l_child==None and tree.r_child==None:
        return tree
    elif tree.value[tree.d]<=value[tree.d]:
        if tree.l_child!=None:
            return find_approx_nearest(tree.l_child,value)
        else:
            return tree
    else:
        if tree.r_child!=None:
            return find_approx_nearest(tree.r_child,value)
        else:
            return tree

exampletree=build_tree(dict(enumerate(np.random.rand(100,3).tolist())))


print(find_approx_nearest(exampletree,[0.2,0.7,0.9]))

def find_exact_nearest(tree,value):
    return print("not defined")

def add_node(tree,value):
    return print("not defined")
