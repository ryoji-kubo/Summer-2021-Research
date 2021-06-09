"""
This file calculates the Krachhardt Hierarchy score for each training data.
The output is in the respective output file. 
The score is given for each relation in each directed graph.

This file reads the test data instead of train data for practical reasons. 
Replace the test file name with the corresponding train file name.
"""


import numpy as np
import networkx as nx
import curvEstimate
import KHierarchy as K
import readGraph as rg

print("calculating Krachhardt Hierarchy score...")

G_dir_list, relations_dir = rg.readGraphDir("train_WN18RR.txt")
# print(f"relations_dir: {relations_dir}")
KHs_list = []
f = open("KHs_WN18RR.txt", "w")
for index in range(len(relations_dir)):
    KHs = K.KHs(G_dir_list[index])
    KHs_list.append(KHs)
    f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
    # print(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}")
f.close()
print("Completed WN18RR")


# G_dir_list, relations_dir = rg.readGraphDir("test_MetaQA.txt")
# # print(f"relations_dir: {relations_dir}")

# KHs_list = []
# f = open("KHs_MetaQA.txt", "w")
# for index in range(len(relations_dir)):
#     KHs = K.KHs(G_dir_list[index])
#     KHs_list.append(KHs)
#     f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
#     # print(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}")
# f.close()
# print("Completed MetaQA")


# G_dir_list, relations_dir = rg.readGraphDir("test_MetaQA_half.txt")
# # print(f"relations_dir: {relations_dir}")
# KHs_list = []
# f = open("KHs_MetaQA_half.txt", "w")
# for index in range(len(relations_dir)):
#     KHs = K.KHs(G_dir_list[index])
#     KHs_list.append(KHs)
#     f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
#     # print(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}")
# f.close()
# print("Completed MetaQA_half")

# G_dir_list, relations_dir = rg.readGraphDir("test_fbwq_full.txt")
# # print(f"relations_dir: {relations_dir}")
# KHs_list = []
# f = open("KHs_fbwq_full.txt", "w")
# for index in range(len(relations_dir)):
#     KHs = K.KHs(G_dir_list[index])
#     KHs_list.append(KHs)
#     f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
# f.close()
# print("Completed fbwq_full")

# G_dir_list, relations_dir = rg.readGraphDir("test_fbwq_half.txt")
# # print(f"relations_dir: {relations_dir}")
# KHs_list = []
# f = open("KHs_fbwq_half.txt", "w")
# for index in range(len(relations_dir)):
#     KHs = K.KHs(G_dir_list[index])
#     KHs_list.append(KHs)
#     f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
# f.close()
# print("Completed fbwq_half")
print("Work Completed")


