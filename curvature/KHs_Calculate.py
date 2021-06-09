import numpy as np
import networkx as nx
import curvEstimate
import KHierarchy as K
import readGraph as rg

print("calculating Krachhardt Hierarchy score...")
# G_undir_list, relations_undir = rg.readGraphUndir("MetaQA_Test.txt")
G_dir_list, relations_dir = rg.readGraphDir("testMetaQA.txt")

# print(f"relations_undir: {relations_undir}")
# print(f"relations_dir: {relations_dir}")

KHs_list = []
f = open("KHs_MetaQA.txt", "w")
for index in range(len(relations_dir)):
    KHs = K.KHs(G_dir_list[index])
    KHs_list.append(KHs)
    f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
    # print(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}")
f.close()

G_dir_list, relations_dir = rg.readGraphDir("testMetaQA_half.txt")
print(f"relations_dir: {relations_dir}")
KHs_list = []
f = open("KHs_MetaQA_half.txt", "w")
for index in range(len(relations_dir)):
    KHs = K.KHs(G_dir_list[index])
    KHs_list.append(KHs)
    f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
    # print(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}")
f.close()

G_dir_list, relations_dir = rg.readGraphDir("testfbwq_full.txt")
print(f"relations_dir: {relations_dir}")
KHs_list = []
f = open("KHs_fbwq_full.txt", "w")
for index in range(len(relations_dir)):
    KHs = K.KHs(G_dir_list[index])
    KHs_list.append(KHs)
    f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
f.close()

G_dir_list, relations_dir = rg.readGraphDir("testfbwq_half.txt")
print(f"relations_dir: {relations_dir}")
KHs_list = []
f = open("KHs_fbwq_half.txt", "w")
for index in range(len(relations_dir)):
    KHs = K.KHs(G_dir_list[index])
    KHs_list.append(KHs)
    f.write(f"relation: {relations_dir[index]}, KHs: {KHs_list[index]}\n")
f.close()
print("Work Completed")


