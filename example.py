import numpy as np
import kd_tree as kd
import json

# generate 1000 random data points and building a tree from them
exampletree=kd.build_tree(dict(enumerate(np.random.rand(1000,4).tolist())))
# finding the approximate nearest neighbor and its distance to a value
print(kd.distance(kd.find_approx_nearest(exampletree,[0.2,0.7,0.9,0.5]).value,
            [0.2,0.7,0.9,0.5]),
    kd.find_approx_nearest(exampletree,[0.2,0.7,0.9,0.5]).value)
# finding the exact nearest neighbor
print(kd.find_exact_nearest(exampletree,[0.2,0.7,0.9,0.5]))

# importing a dataset of paint colors and their position in the XXX colorspace
with open ("paintcolors.json") as json_file:
    paintcolors=json.load(json_file)
# creating a tree out of the paintcolors
painttree=kd.build_tree(paintcolors)
# finding the nearest color to [0,0,0]
print(kd.find_exact_nearest(painttree,[0,0,0]))
