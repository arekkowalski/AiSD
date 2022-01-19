from enum import Enum
from typing import Any
from typing import Tuple
from typing import Optional
from typing import Callable
from typing import Dict, List
import graphviz
import math

counter: int = 1

def visit(something: Any) -> None:
    print(f'v{something.index}')

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    i: int = 0
    data: Any
    index: int

    def __init__(self, data: Any) -> None:
        self.data = data
        self.index = Vertex.i
        Vertex.i += 1

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def getVertex(self, value: str) -> Vertex:
        for v in self.adjacencies.keys():
            if v.data == value:
                return v

    def undirected(self) -> bool:
        first: Vertex = next(iter(self.adjacencies))
        for edge in self.adjacencies[first]:
            for _edge in self.adjacencies[edge.destination]:
                if _edge.destination == first:
                    return True
        return False

    def __init__(self) -> None:
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> None:
        self.adjacencies[Vertex(data)] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.__add(EdgeType(1), source, destination, weight)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.__add(EdgeType(2), source, destination, weight)

    def __add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == edge.directed:
            self.adjacencies[source].append(Edge(source, destination, weight))

        else:

            self.adjacencies[source].append(Edge(source, destination, weight))
            self.adjacencies[destination].append(Edge(destination, source, weight))

    def show(self) -> None:
        global counter
        f = graphviz.Digraph('graph', filename=f'graph{counter}.gv')
        counter += 1

        for i in iter(self.adjacencies):
            f.node(f'{i.data}')

        for _list in list(self.adjacencies.values()):
            for e in _list:
                weight: str = ''
                if (e.weight):
                    weight = e.weight
                f.edge(f'{e.source.data}', f'{e.destination.data}', label=f'{weight}', arrowhead = 'normal')
        f.view()


def friend_path(g: Graph, _f0: Any, _f1: Any) -> List[Any]:
        f0 = g.getVertex(_f0)
        f1 = g.getVertex(_f1)

        queue: List[Vertex] = [f0]
        visited: List[Vertex] = [f0]
        result: Dict = {}
        while (len(queue) != 0):
            currentVertex: Vertex = queue.pop(0)
            for np in g.adjacencies[currentVertex]:
                if np.destination in visited:
                    continue
                else:
                    queue.append(np.destination)
                    visited.append(np.destination)
                    result[np.destination] = currentVertex

        #tmp1 = list(result.keys())
        #tmp2 = list(result.values())

        finalResult: List[Vertex] = [f1]
        for i in range(0, len(finalResult)):
            finalResult.append(result[finalResult[i]])
        finalResult.append(f0)
        return finalResult


# graph1: Graph = Graph()
#
# graph1.create_vertex("A")
# graph1.create_vertex("B")
# graph1.create_vertex("C")
# graph1.create_vertex("D")
# graph1.create_vertex("E")
# graph1.create_vertex("F")
# graph1.create_vertex("G")
# graph1.create_vertex("H")
# graph1.create_vertex("I")
#
# graph1.add_undirected_edge(graph1.getVertex("A"), graph1.getVertex("B"))
# graph1.add_undirected_edge(graph1.getVertex("B"), graph1.getVertex("C"))
# graph1.add_undirected_edge(graph1.getVertex("C"), graph1.getVertex("F"))
# graph1.add_undirected_edge(graph1.getVertex("F"), graph1.getVertex("I"))
# graph1.add_undirected_edge(graph1.getVertex("A"), graph1.getVertex("D"))
# graph1.add_undirected_edge(graph1.getVertex("D"), graph1.getVertex("G"))
# graph1.add_undirected_edge(graph1.getVertex("G"), graph1.getVertex("H"))
# graph1.add_undirected_edge(graph1.getVertex("H"), graph1.getVertex("I"))
# graph1.add_undirected_edge(graph1.getVertex("A"), graph1.getVertex("E"))
# graph1.add_undirected_edge(graph1.getVertex("E"), graph1.getVertex("I"))
#
# graph1.show()
#
# print("Friend path for A and I / graph1 ", end = '')
# result_graph1 = friend_path(graph1, "A", "I")
# for v in result_graph1:
#     print(v.data, end = ", ")
# print()
#
# graph2: Graph = Graph()
#
# graph2.create_vertex("A")
# graph2.create_vertex("B")
# graph2.create_vertex("C")
# graph2.create_vertex("D")
# graph2.create_vertex("E")
#
# graph2.add_undirected_edge(graph2.getVertex("A"), graph2.getVertex("B"))
# graph2.add_undirected_edge(graph2.getVertex("B"), graph2.getVertex("C"))
# graph2.add_undirected_edge(graph2.getVertex("D"), graph2.getVertex("C"))
# graph2.add_undirected_edge(graph2.getVertex("D"), graph2.getVertex("E"))
# graph2.add_undirected_edge(graph2.getVertex("B"), graph2.getVertex("E"))
#
# graph2.show()
#
# print("Friend path for A and C / graph2 ", end = '')
# result_graph1 = friend_path(graph2, "A", "C")
# for v in result_graph1:
#    print(v.data, end = ", ")
# print()
#
# graph3: Graph = Graph()
#
# graph3.create_vertex("A")
# graph3.create_vertex("B")
# graph3.create_vertex("C")
# graph3.create_vertex("D")
# graph3.create_vertex("E")
#
# graph3.add_undirected_edge(graph3.getVertex("A"), graph3.getVertex("B"))
# graph3.add_undirected_edge(graph3.getVertex("B"), graph3.getVertex("C"))
# graph3.add_undirected_edge(graph3.getVertex("D"), graph3.getVertex("C"))
# graph3.add_undirected_edge(graph3.getVertex("D"), graph3.getVertex("E"))
#
# graph3.show()
#
# print("Friend path for B and E / graph3: ", end = '')
# result_graph2 = friend_path(graph3, "B", "E")
# for v in result_graph1:
#    print(v.data, end = ", ")
# print()