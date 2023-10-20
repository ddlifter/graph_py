from graph import Graph
from dfs import dfs, dfs_t
from trans import trans_
from init_graph import init_Graph, VERTEX

graph = Graph()

init_Graph(graph)

order : list[int] = []
used : list[bool] = [False]*graph.count_v()
component = []

for i in range(graph.count_v()):
    if not used[i]:
        dfs(i, order, used, graph)


graph_t = Graph.get_transpose_graph(graph)


used : list[bool] = [False]*graph.count_v()

for i in range(graph.count_v()):
    v = order[graph.count_v() - i - 1]

    if not used[v]:
        dfs_t(v, component, used, graph_t)

        print("".join([VERTEX[index] + " " for index in component]))

        component.clear()


print("--------")

trans_(graph)




