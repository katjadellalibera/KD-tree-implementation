import numpy as np
import kd_tree as kd
import json

exampletree=kd.build_tree(dict(enumerate(np.random.rand(1000,3).tolist())))
print(kd.distance(kd.find_approx_nearest(exampletree,[0.2,0.7,0.9]).value,
            [0.2,0.7,0.9]),
    kd.find_approx_nearest(exampletree,[0.2,0.7,0.9]).value)
print(kd.find_exact_nearest(exampletree,[0.2,0.7,0.9]))

paintcolors=
