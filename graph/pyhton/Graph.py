from collections import defaultdict


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


# class AdjacencyNode:
#     def __init__(self, vertex:Vertex):
#         self.data = vertex
#         self.next = None


class Graph:
    def __init__(self, name: str):
        self.name = name
        self.vertices = list()
        self.edges = defaultdict(list)

    def addVertex(self, name, value):
        """add a vertix to this graph

        Args:
            name (str): name of the vertex
            value (int): value of the vertex

        Returns:
            Vertex: the creted vertex
        """
        v = Vertex(self, name, value)
        self.vertices.append(v)
        return v

    def addEdge(self, name, weight, from_vertex, to_vertex, directed):
        """a method to add a edge to the existing graph 

        Args:
            name (str): name of the Edge
            weight (int): wieght of the Edge
            from_vertex (Vertex): start of the edge
            to_vertex (vertex): end of the edge
            directed (bool): a flag to defined the type of edge

        Returns:
            null/ exception: _description_
        """
        if from_vertex.graph == to_vertex.graph:
            e = Edge(name, weight, from_vertex, to_vertex, directed)
            self.edges[from_vertex].append(e)
            if not directed:
                self.edges[to_vertex].append(e)
            return e
        assert False, "vertices should be in same graph"

    def findParent(self, subset, vertex):
        if subset[vertex].parent == vertex:
            return vertex
        return self.findParent(subset, subset[vertex].parent)

    def union(self, subset, vertex1, vertex2):
        vertex1 = self.findParent(subset, vertex1)
        vertex2 = self.findParent(subset, vertex2)
        if subset[vertex1].rank > subset[vertex2].rank:
            subset[vertex2].parent = vertex1
        elif subset[vertex2].rank > subset[vertex1].rank:
            subset[vertex1].parent = vertex2
        else:
            subset[vertex2].parent = vertex1
            subset[vertex1].rank += 1

    def isCycle(self):
        parent_subset = {}
        for vertex in self.vertices:
            parent_subset[vertex] = Subset(vertex, 0)
        for vertex in self.edges:
            x = self.findParent(parent_subset, vertex)
            for neighbor in self.edges[vertex]:
                y = self.findParent(parent_subset, neighbor.to_vertex)
                if x == y:
                    return True
                else:
                    self.union(parent_subset, x, y)
        return False

    def DFSUtil(self, root, visited):
        visited.append(root)
        for neighbor in self.edges[root]:
            if neighbor.to_vertex not in visited:
                self.DFSUtil(neighbor.to_vertex, visited)
            elif neighbor.from_vertex not in visited:
                self.DFSUtil(neighbor.from_vertex, visited)

    def DFS(self):
        visited = list()
        for vertex in self.vertices:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)
        return visited

    def BFS(self, root):
        visited = list()
        queue = list()
        queue.append(root)
        visited.append(root)
        while queue:
            start = queue.pop(0)
            for neighbor in self.edges[start]:
                if neighbor.to_vertex not in visited:
                    queue.append(neighbor.to_vertex)
                    visited.append(neighbor.to_vertex)
                elif neighbor.from_vertex not in visited:
                    queue.append(neighbor.from_vertex)
                    visited.append(neighbor.from_vertex)

        return visited

    def topologicalSort(self):
        pass

    def kruskalMST(self):
        result = list()
        parent_subset = {}
        for vertex in self.vertices:
            parent_subset[vertex] = Subset(vertex, 0)

        edges = [edge for x in self.edges.keys() for edge in self.edges[x]]
        edges = sorted(edges, key=lambda x: x.weight)

        for edge in edges:
            x = self.findParent(parent_subset, edge.from_vertex)
            y = self.findParent(parent_subset, edge.to_vertex)
            if x != y:
                result.append(edge)
                self.union(parent_subset, edge.from_vertex, edge.to_vertex)

        minimum_cost = 0
        for edge in result:
            minimum_cost += edge.weight
        return minimum_cost

    def __str__(self):
        intro = "*" * 30 + "\n"
        name = f"Graph:{self.name}\n"
        vertices = "vertices = ["
        for vertex in self.vertices:
            vertices += str(vertex) + ", "
        vertices += "]\n"
        edges = "edges = { \n"
        for vertex in self.edges:
            for edge in self.edges[vertex]:
                edges += str(edge) + "\n"
        edges += "}\n"
        outro = "*" * 30
        return intro + name + vertices + edges + outro


class Vertex:  # also known as Node or Point
    def __init__(self, graph: Graph, name: str, value: int):
        self.graph = graph
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}({self.value})"


class Edge:  # also knows as links or Lines
    def __init__(
        self,
        name: str,
        weight: int,
        from_vertex: Vertex,
        to_vertex: Vertex,
        directed: bool = False,
    ):
        self.name = name
        self.weight = weight
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.directed = directed

    def __str__(self):
        if self.directed:
            return f"{self.name}: {self.from_vertex} -{self.weight}-> {self.to_vertex} "
        else:
            return (
                f"{self.name}: {self.from_vertex} <-{self.weight}-> {self.to_vertex} "
            )


if __name__ == "__main__":
    g = Graph("DFS")
    v0 = g.addVertex("0", 0)
    v1 = g.addVertex("1", 0)
    v2 = g.addVertex("2", 0)
    v3 = g.addVertex("3", 0)
    v4 = g.addVertex("4", 0)
    v5 = g.addVertex("5", 0)
    v6 = g.addVertex("6", 0)
    v7 = g.addVertex("7", 4)
    v8 = g.addVertex("8", 0)

    g.addEdge("01", 4, v0, v1, directed=False)
    g.addEdge("02", 8, v0, v2, directed=False)
    g.addEdge("03", 11, v0, v3, directed=False)
    g.addEdge("14", 8, v4, v1, directed=False)
    g.addEdge("25", 1, v2, v5, directed=False)
    g.addEdge("26", 7, v2, v6, directed=False)
    g.addEdge("37", 6, v3, v7, directed=False)
    g.addEdge("78", 2, v7, v8, directed=False)

    bfs = g.BFS(v0)
    expect = [vertex.name for vertex in bfs]
    actual = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    print(*bfs)
