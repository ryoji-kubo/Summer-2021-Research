import networkx as nx
import numpy as np
"""
- This is the modified implementation of the curvature estimate taken from https://github.com/HazyResearch/hyperbolics/blob/274b6af552e1f4dfa247b297342e24a91b5e5344/curv.py
- See Appendix A.2 of "Low-Dimensional Hyperbolic Knowledge Graph Embeddings" for the calculation
- See "Learning Mixed-Curvature Representations in Product Spaces" for the detailed proof and calculation

How to calcute the curvature estimate:
1. Create a list of undirected graphs Gr spanned by edges labeled as r
2. For each Gr, get the list of Connected Components (C), Distance Matrix D (indicates the distance bet. 2 nodes on Gr, and list of number of Nodes for each Component (N))
3. Calculate the Weight for each Connected Component by (n_i)^3/sum((n_i)^3) where n_i is the corresponding number of nodes in Component i
4. Itirate over each Component:
	- Randomly sample 1000*(w_i) triangles where w_i is the corresponding Weight for Component i
	- Calculate curvature estimate for all the sampled triangles
	- Get the average of Curvature estimate for Component
5. The Curvature Estimate for Gr is the average of Curvature estimate of all components
6. Repeat 2 - 5 for all other Gr (other types of relation)


What I have not implemented yet ( indicated in estimate() )
- Create a list of undirected graphs Gr spanned by edges labeled as r
- Distance Matrix D
- The weighted average of the Curvature Estimate for the entire relations (the whole graph)
"""

#function to calculate curvature estimate for a single triangle {a, b, c}
def Ka(D, m, b, c, a):
    if a == m: return 0.0
    k = D[a][m]**2 + D[b][c]**2/4.0 - (D[a][b]**2 + D[a][c]**2)/2.0
    k /= 2*D[a][m]
    # print(f'{m}; {b} {c}; {a}: {k}')
    return k

#function to sample 1000*W[i] triangles from a connected component and calculate the curvature estimate for each
def sample_G(component, D, n, w):	#Parameters: the connected component, distance matrix, number of nodes, weight
    samples = []                                    #This will contain the curvature estimates for all the sampled triangles
    _cnt = 0
    while _cnt < 1000*w:                         	
        m = np.random.randint(0, n)                 #pick randomly m, the midpoint of the shortest path connecting b to c (b, c will be m's two neighbors)
        edges = list(G.edges(m))                    
        # print(f"edges of {m}: {edges}")
        i = np.random.randint(0, len(edges))        #pick a random node (2nd node of the triangle, node b)
        j = np.random.randint(0, len(edges))        #pick a random node (3rd node of the triangle, node c)
        b = edges[i][1]
        c = edges[j][1]
        if b==c: continue
        a = np.random.randint(0, n)                 #pick a randdom node (1st node of the triangle, node a)
        k = Ka(D, m, b, c, a)                       #calculate the curvature estimate for that function.
        samples.append(k)                           
        # print(k)

        _cnt += 1

    return np.array(samples)


def estimate(dataset='data/edges/smalltree.edges', n_samples=100000):
    G = load_graph.load_graph(dataset)	#load the entire graph
    n = G.order()
    num_workers = 16
    D   = gh.build_distance(G, 1.0, num_workers) # load the whole matrix (the distance matrix)

    """
    TODO HERE:
    1. Find undirected graph Gr spanned by edges labeled as r, create G_list which holds Gr for all r
	2. Create the distance matrix D which gets the distance between two nodes on Gr
	3. Loop through the following instructions for each undirected graph Gr for each relation r
    """


    for Gr in G_list:
    	curv_estimates = []

    	# ==== Insert code to find D here ===

    	C = [Gr.subgraph(component).copy() for component in nx.connected_components(Gr)]	#get the list of connected components of Gr
    	N = np.array([component.order() for component in C])		#get the number of nodes in each component
   		N_cube = np.power(N,3)		
   		N_sum = np.sum(N_cube)				#the normalizing factor

   		W = 1/N_sum * N_cube		#The list of Weights	

    	index = 0
    	for component in C:
    		samples = sample_G(component, D, N[index], W[index])
    		avg = np.mean(samples)
    		curv_estimates.append(avg)
    		index += 1;
    	curv_estimates = np.array(curv_estimates)
    	Gr_curve = np.mean(curv_estimates)


    # ==== Calculate the Weighted average of Curvature Estimate for the Whole Graph ===




"""
For reference: how HazyResearch implements distance matrix from the helper functions
https://github.com/HazyResearch/hyperbolics/blob/dedf0511f715a02152ba9287439a75c33aca2ef4/pytorch/graph_helpers.py#L12
"""

def djikstra_wrapper( _x ):
    (mat, x) = _x
    return csg.dijkstra(mat, indices=x, unweighted=False, directed=False)

def build_distance(G, scale, num_workers=None):
    n = G.order()
    p = Pool() if num_workers is None else Pool(num_workers)
    
    #adj_mat_original = nx.to_scipy_sparse_matrix(G)
    adj_mat_original = nx.to_scipy_sparse_matrix(G, nodelist=list(range(G.order())))

    # Simple chunking
    nChunks     = 128 if num_workers is not None and num_workers > 1 else n
    if n > nChunks:
        chunk_size  = n//nChunks
        extra_chunk_size = (n - (n//nChunks)*nChunks)
            

        chunks     = [ list(range(k*chunk_size, (k+1)*chunk_size)) for k in range(nChunks)]
        if extra_chunk_size >0: chunks.append(list(range(n-extra_chunk_size, n)))
        Hs = p.map(djikstra_wrapper, [(adj_mat_original, chunk) for chunk in chunks])
        H  = np.concatenate(Hs,0)
        logging.info(f"\tFinal Matrix {H.shape}")
    else:
        H = djikstra_wrapper( (adj_mat_original, list(range(n))) )
        
    H *= scale
    return H












