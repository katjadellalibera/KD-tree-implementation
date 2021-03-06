import numpy as np
import math
import random as random

class Node:

    def __init__(self,name,value,l_child,r_child,d):
        """
        definition of a node and its properties
        """
        self.name=name
        self.value=value
        self.l_child=l_child
        self.r_child=r_child
        self.d=d

    def __str__(self):
        """
        how to display a tree: every new level is indented
        example input:
        print(build_tree({"a":[1,1,1],"b":[3,5,2],"c":[3,5,7],"d":[5,1,2]}))
        example output:
        name: c, value: [3, 5, 7], d: 0
	       name: b, value: [3, 5, 2], d: 1
		         name: a, value: [1, 1, 1], d: 2
			              None
			              None
		         None
	       name: d, value: [5, 1, 2], d: 1
		         None
		         None
        """
        return "\t".join(str("name: {}, value: {}, d: {}  \n{}  \n{} ".format(
            self.name,self.value,self.d,self.l_child,self.r_child))
            .splitlines(True))


def build_tree(dictionary,d=0):
    """
    Function to build a tree from a dictionary of names and values
    """
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
    """
    function to very quickly find an approximation for the nearest neighbor
    it may not be exact if the point is close to one of the pivot points,
    because the nearest neighbor may be excluded prematurely
    """
    if tree.l_child==None and tree.r_child==None:
        return tree
    elif tree.value[tree.d]>=value[tree.d]:
        if tree.l_child!=None:
            return find_approx_nearest(tree.l_child,value)
        else:
            return tree
    else:
        if tree.r_child!=None:
            return find_approx_nearest(tree.r_child,value)
        else:
            return tree

def distance(lsta, lstb):
    """
    Finds the distance between two coordinates in k dimensions with coordinates
    described as lists
    """
    if len(lsta)!=len(lstb):
        return "Error: wrong dimensions"
    return math.sqrt(sum([(lsta[i]-lstb[i])**2 for i in range(len(lsta))]))



def find_exact_nearest(tree,value):
    """
    finds the exact nearest neighbor by searching any node that is approximately
    as close as the nearest neighbor
    """
    closest=find_approx_nearest(tree,value)
    approx=closest.value
    dist=distance(approx,value)

    def find_exact_nearest_helper(tree,value):
        """
        helper function to find the exact nearest neighbor
        """
        nonlocal dist
        nonlocal closest
        if dist>distance(tree.value,value):
            closest=Node(tree.name,tree.value,None,None,None)
            dist=distance(tree.value,value)
        if dist>abs(tree.value[tree.d]-value[tree.d]):
            if tree.l_child!=None:
                find_exact_nearest_helper(tree.l_child,value)
            if tree.r_child!=None:
                find_exact_nearest_helper(tree.r_child,value)
        if dist<abs(tree.value[tree.d]-value[tree.d]):
            if tree.value[tree.d]>=value[tree.d]:
                if tree.l_child!=None:
                    find_exact_nearest_helper(tree.l_child,value)
            else:
                if tree.r_child!=None:
                    find_exact_nearest_helper(tree.r_child,value)
    find_exact_nearest_helper(tree,value)
    return (dist,closest.name,closest.value)
