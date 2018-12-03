from collections import namedtuple
from operator import itemgetter
from pprint import pformat

class Node(namedtuple("Node","location left_child right_child")):
    # how to represent the node:
    def __repr__(self):
        return pformat(tuple(self))

# creating a kd=tree out of the list of values
def kd_tree(lst,depth=0):
    # letting 
    if lst==None:
        return None
    else:
        # determining how many dimensions the points have
        k=len(lst[0])
    # determining which dimension to consider in the current iteration of kd_tree
    dimension=depth%k
    # sorting the list with the dimension as criterion and choosing the median as pivot
    lst.sort(key=itemgetter(dimension))
    pivot=len(lst)//2
    # recursively calling the function to create the tree
    return Node(
        location=lst[pivot],
        left_child=kd_tree(lst[:pivot],depth+1),
        right_child=kd_tree(lst[pivot+1:],depth+1)
    )

def approximate_nearest(tree,elem):

def exact_nearest(tree,elem):

def
