from graph import Graph
from init_graph import init_Graph, matrix

def trans_(graph: Graph):
    trans_matrix = [[0] * graph.count_v() for i in range(graph.count_v())]
    for i in range(graph.count_v()):
        for j in range(graph.count_v()):
            trans_matrix[i][j] = matrix[i][j]


    for k in range(graph.count_v()):
        for i in range(graph.count_v()):
            for j in range(graph.count_v()):
                trans_matrix[i][j] = trans_matrix[i][j] or (trans_matrix[i][k] and trans_matrix[k][j])

    
    for i in range(graph.count_v()):
        trans_matrix[i][i] = 1
        for j in range(graph.count_v()):
            trans_matrix[i][j] = trans_matrix[i][j] and trans_matrix[j][i]

    
    ssk = []
    for i in trans_matrix:
        if i not in ssk:
            ssk.append(i)

    for i in range(len(ssk)):
        res = []
        for j in range(graph.count_v()):
            if ssk[i][j] == 1:
                res.append(j)
        print(*res)

