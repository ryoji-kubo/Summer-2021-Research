"""
The following is the vectorized implementation fo the Krachhardt Hierarchy score.
See Appendix A.2 of "Low-Dimensional Hyperbolic Knowledge Graph Embeddings" for the calculation

For more details, see "Graph theoretical dimensions of informal organizations." by David Krachhardt

Krachhardt Hierarchy score captures local behaviour (how many small loops the graph has).
Hierarchy measures quantify the extent of asymmetry in a structure; the greater the extent of asymmetry, the more hierarchical the structure is said to be.

This could be used along with the curvEstimate, the lower the global curvEstimate, the graph is more tree-like globally. 
The higher the KHs, the more asymetric it is. (0 <= KHs <= 1)

The input to this function should be Gr, where Gr is the undirected graphs spanned by edges labeled as r.

"""
import networkx as nx
import numpy as np

def KHs(Gr):
	R = np.array(nx.adjacency_matrix(Gr).todense())
	denominator = R.sum()
	numerator = (R*(1-R).T).sum()
	numerator = float(numerator)
	KHs = numerator/denominator
	# print(KHs)
	return KHs