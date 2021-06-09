import networkx as nx

def readGraphUndir(fname):
    file = open(fname, 'r')

    relations = []
    G_list = []

    for line in file:
        data = line.strip().split("	")
        if data[1] in relations:
            index = relations.index(data[1])
            G_list[index].add_edge(data[0],data[2],relation=data[1])
        else:
            relations.append(data[1])
            G_list.append(nx.Graph())
            index = relations.index(data[1])
            G_list[index].add_edge(data[0],data[2],relation=data[1])

    file.close()
    return G_list, relations

def readGraphDir(fname):
    file = open(fname, 'r')

    relations = []
    G_list = []

    for line in file:
        data = line.strip().split("	")
        if data[1] in relations:
            index = relations.index(data[1])
            G_list[index].add_edge(data[0],data[2],relation=data[1])
        else:
            relations.append(data[1])
            G_list.append(nx.DiGraph())
            index = relations.index(data[1])
            G_list[index].add_edge(data[0],data[2],relation=data[1])

    file.close()
    return G_list, relations
