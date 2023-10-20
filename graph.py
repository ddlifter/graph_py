from __future__ import annotations

class Graph:
    __matrix: list[list[int]] = []

    def __init__(self, matrix: list[list[int]] = None):
        if matrix is None:
            matrix = []

        self.__matrix = matrix

    
    def __getitem__(self, key) -> list[int]:
        return self.__matrix[key]
    

    @staticmethod
    def get_transpose_graph(graph: Graph) -> Graph:
        matrix = [[0] * graph.count_v() for i in range(graph.count_v())]

        for row_index in range(graph.count_v()):
            row = graph[row_index]
            for col_index, col_value in enumerate(row):
                matrix[col_index][row_index] = col_value

        return Graph(matrix=matrix)
    
    def count_v(self):
        return len(self.__matrix)
    

    def add_v(self, name: str, mark: int):
        for row in self.__matrix:
            row.append(0)

        self.__matrix.append([0] * (self.count_v() + 1))


    def add_e(self, v: int, w: int, c: int = 1):
        if v > self.count_v():
            raise Exception(f'Incorrect v: index is overflow. Size: {self.count_v()}, index v {v}')
        
        if w > len(self.__matrix[v]):
            raise Exception(f'Incorrect w: index is overflow! Size: {self.count_v()}, index w {w}')
        
        self.__matrix[v][w] = c

    
    def output(self):
        for i in self.__matrix:
            print(*i)

    
    def del_v(self, name: str):
        index = int(name)

        for row in self.__matrix:
            row.pop(index)

        self.__matrix.pop(index)

    
    def vertex(self, v: int, i:int):
        for index in self.__matrix[v]:
            if index == i:
                return 

        
        