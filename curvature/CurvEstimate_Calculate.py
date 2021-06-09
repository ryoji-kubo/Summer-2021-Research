import numpy as np
import networkx as nx
import curvEstimate
import KHierarchy as K
import readGraph as rg

G_undir_list, relations_undir = rg.readGraphDir("train_WN18RR.txt")
