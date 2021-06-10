"""
Following is the implementation of Curvature Estimate.

"""

import numpy as np
import networkx as nx
import curvEstimate
import readGraph as rg

G_undir_list, relations_undir = rg.readGraphUndir("train_WN18RR.txt")	#Read the Undirected Graph
for index in range(len(relations_undir)):
	print(f"relation: {relations_undir[index]}, numNodes: {G_undir_list[index].order()}")

relation_estimates = curvEstimate.estimate(G_undir_list)

f = open("curve_WN18RR.txt", "w")
for index in range(len(relations_undir)):
	f.write(f"relation: {relations_undir[index]}, curveEstimate: {relation_estimates[index]}\n")
f.close()
print("Completed WN18RR")