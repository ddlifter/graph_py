from graph import Graph

#1 граф

COUNT = 10 #Количество вершин
VERTEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] #Вершины


#Иниициализируем матрицу смежности вручную для метода транзитивного замыкания
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

#Заполнение графа
def init_Graph(graph : Graph):
    for i in range(COUNT):
        graph.add_v(VERTEX[i], mark=i)

    graph.add_e(0, 0)
    graph.add_e(0, 1)
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


#2 граф

COUNT2 = 8 #Количество вершин
VERTEX2 = ["0", "1", "2", "3", "4", "5", "6", "7"] #Вершины

#Иниициализируем матрицу смежности вручную для метода транзитивного замыкания
matrix2 = [[0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 1, 1, 0, 0],
           [0, 0, 0, 1, 0, 0, 1, 0],
           [0, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0, 0, 1, 0]]
           

#Заполнение графа
def init_Graph2(graph: Graph):
    for i in range(COUNT2):
        graph.add_v(name=VERTEX2[i], mark=i)

    graph.add_e(v=0, w=1)  
    graph.add_e(v=1, w=2)  
    graph.add_e(v=2, w=3)  
    graph.add_e(v=3, w=2)  
    graph.add_e(v=1, w=4)  
    graph.add_e(v=4, w=0)  
    graph.add_e(v=1, w=5)  
    graph.add_e(v=4, w=5)  
    graph.add_e(v=5, w=6)  
    graph.add_e(v=6, w=5)  
    graph.add_e(v=2, w=6)  
    graph.add_e(v=3, w=7)  
    graph.add_e(v=7, w=3)  
    graph.add_e(v=7, w=6)  
