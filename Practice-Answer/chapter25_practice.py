class Graph:
    def __init__(self):
        self.neighborList = {}              # 인접한 이웃 node list

    def __iter__(self):
        return iter(self.neighborList.items())     # 인접한 이웃 node list iterable object 반환

    def add_vertex(self, vertex):                    # 그래프에 새로운 node 추가
        if not vertex in self.neighborList:
            self.neighborList[vertex] = []            # 새로이 추가된 node 에는 아직 edge 가 없음

    def add_edge(self, v1, v2, weight):           # 새로운 edge 등록 (이웃 node 와 가중치)
        self.neighborList[v1].append({'node': v2, 'weight': weight})
        self.neighborList[v2].append({'node': v1, 'weight': weight})

g = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a','b',7)
g.add_edge('a','c',9)
g.add_edge('a','f',14)
g.add_edge('b','c',10)
g.add_edge('b','d',15)
g.add_edge('c','d',11)
g.add_edge('c','f',2)
g.add_edge('d','e',6)
g.add_edge('e','f',9)

def connect(a, b, c):
    def dist(x, y):
        for n in g.neighborList[x]:
            if n['node'] == y:
                return n['weight']
        return 0
    return dist(a, b) + dist(b, c)

print(connect('a', 'b', 'c'))
