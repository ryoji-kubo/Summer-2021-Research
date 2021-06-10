"""
Following is the implementation of Curvature Estimate.

"""

import numpy as np
import networkx as nx
import curvEstimate
import readGraph as rg

G_undir_list, relations_undir = rg.readGraphUndir("all_WN18RR.txt")	#Read the Undirected Graph

correct_order = ["_member_meronym","_hypernym","_has_part","_instance_hypernym","_member_of_domain_region","_member_of_domain_usage","_synset_domain_topic_of","_also_see","_derivationally_related_form","_similar_to","_verb_group"]
for index in range(len(relations_undir)):
	correct_index = relations_undir.index(correct_order[index])
	print(f"relation: {relations_undir[correct_index]}, numNodes: {G_undir_list[correct_index].order()}")

relation_estimates, curv = curvEstimate.estimate(G_undir_list)

f = open("curve_WN18RR.txt", "w")
f.write(f"Curvature for WN18RR: {curv}\n")
for index in range(len(relations_undir)):
	correct_index = relations_undir.index(correct_order[index])
	f.write(f"relation: {relations_undir[correct_index]}, curveEstimate: {relation_estimates[correct_index]}\n")
f.close()
print("Completed WN18RR")