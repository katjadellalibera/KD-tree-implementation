import kd_tree

exampletree=build_tree(dict(enumerate(np.random.rand(1000,3).tolist())))
print(distance(find_approx_nearest(exampletree,[0.2,0.7,0.9]).value,[0.2,0.7,0.9]),
    find_approx_nearest(exampletree,[0.2,0.7,0.9]).value)
print(find_exact_nearest(exampletree,[0.2,0.7,0.9]))
