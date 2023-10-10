from graph import Graph

def dfs(v: int, order: list[int], used: list[bool], graph: Graph):
    used[v] = True

    for node in range(graph.count_v()):
        if not used[node] and graph[v][node] > 0:
            dfs(v=node, order=order, used=used, graph=graph)


    order.append(v)


