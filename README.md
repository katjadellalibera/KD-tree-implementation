# KD-tree-implementation
An implementation of kd-search trees with functions to find the nearest neighbor, an operation that would take a long time using linear search on large datasets. That is where kd-search trees come in, since they can exclude a larger part of the dataset at once.<br>
This project was created as a final project for the course CS110/Computation: Solving Problems with algorithms.

# Installation guide
Open the Command center and paste the following<br>
```
pip install Katjas-kd-tree
```
# How to run
After installing the package import it by typing<br>
```
import kd_tree as kd
```
You are now able to use the following functions<br>
```
kd.build_tree(dict)
# this will build a kd-tree from a given dictionary of format key:[values]
kd.distance(lsta,lstb)
# returns the distance between two points a and b with coordinates given by lsta and lstb
kd.find_approx_nearest(tree,value)
# returns the approximate nearest neighbor for a given value
kd.find_exact_nearest(tree,value)
# returns the exact nearest element of the tree to the value
```
# Example use case
To find the closest color in a dataset of named colors in the LAB color space. This color space works similar to RBG colors, but is design to let. we cannot use our usual quick-search methods or binary search-trees, since the data has more than 1 dimension and cannot simply be ordered. Therefore, we can create a tree with 3 dimensions, where every new level is split along a new dimension, iterating through all of them as often as needed. This allows us to very quickly get an approximation of the nearest neighbor and with slightly more effort find the exact nearest neighbor quicker than with a linear search.<br>
```
# importing a dataset of paint colors and their position in the LAB colorspace
with open ("paintcolors.json") as json_file:
    paintcolors=json.load(json_file)
# creating a tree out of the paintcolors
painttree=kd.build_tree(paintcolors)
# finding the approximate and exact nearest color to [0,0,0]
print((kd.distance(kd.find_approx_nearest(painttree,[0,0,0]).value,[0,0,0]),
    kd.find_approx_nearest(painttree,[0,0,0]).name,
    kd.find_approx_nearest(painttree,[0,0,0]).value))
print(kd.find_exact_nearest(painttree,[0,0,0]))
```
This will return the approximate and exact nearest color to [0,0,0]<br>
(0.23327147726897515, 'UniversalBlack', [0.233007, 0.010686, -0.0030215])<br>
(0.22615200000001437, 'TwilightZone', [0.226152, 5.54817e-08, 5.84874e-08])<br>
<br>
If you would like to run this code for yourself, please download the data from https://github.com/katjadellalibera/KD-tree-implementation/blob/master/paintcolors.json and the code from https://github.com/katjadellalibera/KD-tree-implementation/blob/master/example.py
# Background
**Complexity:**<br>
A linear search runs with O(n) complexity, since it has to check every value. find_approx_nearest runs with $O(\log(n))$ complexity on average, because it just has to go down a binary tree with a depth of $\log_2(n)$. In the worst case we have a oddly shaped tree like one with only two nodes, where the worst-case runtime could be $O(n)$, because every node is visited. The find_exact_nearest function will exclude less of the tree at a time, but still run in $O(\log(n))$, just with a higher constant factor.
# Dependencies
The implementation depends on a the pre-installed packages random, math and json as well as the numpy package.
