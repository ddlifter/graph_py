from graph import Graph

COUNT = 10
VERTEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

matrix = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
          [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

def init_Graph(graph : Graph):
    for i in range(COUNT):
        graph.add_v(VERTEX[i], mark=i)

    graph.add_e(0, 0)
    graph.add_e(1, 2)
    graph.add_e(1, 3)
    graph.add_e(2, 8)
    graph.add_e(2, 5)
    graph.add_e(2, 3)
    graph.add_e(3, 4)
    graph.add_e(3, 1)
    graph.add_e(4, 1)
    graph.add_e(6, 7)
    graph.add_e(7, 6)
    graph.add_e(8, 9)
    graph.add_e(8, 2)
    graph.add_e(9, 8)