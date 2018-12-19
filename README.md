# KD-tree-implementation
An implementation of kd-search trees with functions to find the nearest neighbor, an operation that would take a long time using linear search on large datasets. That is where kd-search trees come in, since they can exclude a larger part of the dataset at once.<br>
This project was created as a final project for the course CS110/Computation: Solving Problems with algorithms.

#Installation guide
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
To find the closest color in a dataset of named colors, we cannot use our usual quick-search methods or binary search-trees, since the data has more than 1 dimension and cannot simply be ordered. Therefore, we can create a tree with k dimensions, where every new level is split along a new dimension, iterating through all of them as often as needed. This allows us to very quickly get an approximation of the nearest neighbor and with slightly more effort find the exact nearest neighbor quicker than with a linear search.<br>
To find code examples of this use case, open example.py
#Background
**Complexity:**<br>
A linear search runs with O(n) complexity, since it has to check every value. find_approx_nearest runs with O(log(n)) complexity on average. The find_exact_nearest function will exclude less of the tree at a time, but still run in O(log(n)), just with a higher constant factor.
