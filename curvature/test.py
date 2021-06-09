import numpy as np
import networkx as nx
import curvEstimate
import KHierarchy as K
import readGraph as rg

G1 = nx.DiGraph()
G1.add_edges_from([(1,2),(2,3),(3,4)])
KHs_1 = K.KHs(G1)
print("KHs_1: ",KHs_1)

G2 = nx.DiGraph()
G2.add_edges_from([(1,2),(2,3),(3,4),(4,3),(3,2),(2,1)])
KHs_2 = K.KHs(G2)
print("KHs_2: ",KHs_2)

G3 = nx.DiGraph()
G3.add_edges_from([(1,2),(2,3),(3,4),(3,2),(2,1)])
KHs_3 = K.KHs(G3)
print("KHs_3: ",KHs_3)
