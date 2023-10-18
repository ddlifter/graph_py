from graph import Graph
from utils import dfs, dfs_t

COUNT = 8
VERTEX = ["A", "B", "C", "D", "E", "F", "G", "H"]

def init_graph(graph : Graph):
    for i in range(COUNT):
        graph.add_v(VERTEX[i], mark=i)

    # A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7

    graph.add_e(0, 1)
    graph.add_e(1, 2)
    graph.add_e(1, 5)
    graph.add_e(1, 4)
    graph.add_e(2, 3)
    graph.add_e(2, 6)
    graph.add_e(3, 2)
    graph.add_e(3, 7)
    graph.add_e(4, 0)
    graph.add_e(4, 5)
    graph.add_e(5, 6)
    graph.add_e(6, 5)

    if __name__ == '__main__':

        graph = Graph()

        init_graph(graph)

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


