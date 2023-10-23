from graph import Graph
from dfs import dfs_first, dfs_second
from trans import trans_, trans_2
from init_graph import init_Graph, init_Graph2, VERTEX, VERTEX2


print("1 граф")

graph = Graph()

init_Graph(graph)

print("--------------")
print("Решение 1 способом: ")
order : list[int] = []
used : list[bool] = [False]*graph.count_v()
component = []


#Первый обход графа в глубину
for i in range(graph.count_v()):
    if not used[i]:
        dfs_first(i, order, used, graph)


#Транспонируем матрицу
graph_t = Graph.get_transpose_graph(graph)

#Обновляем список пройденных вершин
used : list[bool] = [False]*graph.count_v()

#Проходим граф в глубину во второй раз и выводим сск
for i in range(graph.count_v()):
    v = order[graph.count_v() - i - 1]

    if not used[v]:
        dfs_second(v, component, used, graph_t)

        print("".join([VERTEX[index] + " " for index in component]))

        component.clear()


print("--------------")

print("Решение 2 способом: ")

trans_(graph)

print("\n")

print("##########")

print("\n")

print("2 граф")

graph2 = Graph()

init_Graph2(graph2)

print("--------------")
print("Решение 1 способом: ")
order : list[int] = []
used : list[bool] = [False]*graph2.count_v()
component = []


#Первый обход графа в глубину
for i in range(graph2.count_v()):
    if not used[i]:
        dfs_first(i, order, used, graph2)


#Транспонируем матрицу
graph_t2 = Graph.get_transpose_graph(graph2)

#Обновляем список пройденных вершин
used : list[bool] = [False]*graph2.count_v()

#Проходим граф в глубину во второй раз и выводим сск
for i in range(graph2.count_v()):
    v = order[graph2.count_v() - i - 1]

    if not used[v]:
        dfs_second(v, component, used, graph_t2)

        print("".join([VERTEX2[index] + " " for index in component]))

        component.clear()


print("--------------")

print("Решение 2 способом: ")

trans_2(graph2)

print("--------------")