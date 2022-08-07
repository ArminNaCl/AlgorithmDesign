import unittest
from Graph import *


class TestGraph(unittest.TestCase):
    def __init__(self, methodName) -> None:
        self.graph = Graph(name='name')
        super().__init__(methodName=methodName)

    def testCreateGraph(self):
        return self.assertIsInstance(self.graph, Graph)

    def testAddVertex(self):
        vertex = self.graph.addVertex(name='vertex_test', value=20)
        self.assertIsInstance(vertex, Vertex)
        self.assertIn(vertex, self.graph.vertices)

    def testAddEdge(self):
        vertex1 = self.graph.addVertex(name='vertex_test1', value=20)
        vertex2 = self.graph.addVertex(name='vertex_test2', value=30)
        edge = self.graph.addEdge(name='edge_test', weight=12, from_vertex=vertex1, to_vertex=vertex2, directed=False)
        self.assertIsInstance(edge, Edge)
        self.assertIn(edge, self.graph.edges[vertex1])

    def testFindUnion(self):
        pass

    def testIsCycle1(self):
        g = Graph('a')
        v0 = g.addVertex('0', 0)
        v1 = g.addVertex('1', 0)
        v2 = g.addVertex('2', 0)

        g.addEdge('01', 0, v0, v1, True)
        g.addEdge('12', 0, v1, v2, True)
        g.addEdge('20', 0, v2, v0, True)

        actual = g.isCycle()
        expect = True
        return self.assertEqual(actual, expect)

    def testIsCycle2(self):
        g = Graph('a')
        v0 = g.addVertex('0', 0)
        v1 = g.addVertex('1', 0)
        v2 = g.addVertex('2', 0)
        v3 = g.addVertex('3', 0)

        g.addEdge('01', 0, v0, v1, True)
        g.addEdge('12', 0, v1, v2, True)
        g.addEdge('23', 0, v2, v3, True)

        actual = g.isCycle()
        expect = False
        return self.assertEqual(actual, expect)

    def testKruskalMST(self):
        g = Graph('kruskaltest')
        v0 = g.addVertex('0', 0)
        v1 = g.addVertex('1', 0)
        v2 = g.addVertex('2', 0)
        v3 = g.addVertex('3', 0)
        g.addEdge('01', 10, v0, v1, directed=False)
        g.addEdge('02', 6, v0, v2, directed=False)
        g.addEdge('03', 5, v0, v3, directed=False)
        g.addEdge('13', 15, v1, v3, directed=False)
        g.addEdge('23', 4, v2, v3, directed=False)

        actual = 19
        expect = g.kruskalMST()

        return self.assertEqual(actual, expect)

    def testKruskalMST2(self):
        g = Graph('kruskaltest')
        v0 = g.addVertex('0', 0)
        v1 = g.addVertex('1', 0)
        v2 = g.addVertex('2', 0)
        v3 = g.addVertex('3', 0)
        v4 = g.addVertex('4', 0)
        v5 = g.addVertex('5', 0)
        v6 = g.addVertex('6', 0)
        v7 = g.addVertex('7', 0)
        v8 = g.addVertex('8', 0)

        g.addEdge('01', 4, v0, v1, directed=False)
        g.addEdge('07', 8, v0, v7, directed=False)
        g.addEdge('17', 11, v1, v7, directed=False)
        g.addEdge('12', 8, v1, v2, directed=False)
        g.addEdge('76', 1, v7, v6, directed=False)
        g.addEdge('78', 7, v7, v8, directed=False)
        g.addEdge('68', 6, v6, v8, directed=False)
        g.addEdge('28', 2, v2, v8, directed=False)
        g.addEdge('25', 4, v2, v5, directed=False)
        g.addEdge('65', 2, v6, v5, directed=False)
        g.addEdge('23', 7, v2, v3, directed=False)
        g.addEdge('35', 14, v5, v3, directed=False)
        g.addEdge('34', 9, v4, v3, directed=False)
        g.addEdge('54', 10, v4, v5, directed=False)

        expect = 37
        actual = g.kruskalMST()

        return self.assertEqual(actual, expect)

    def testDFS(self):
        g = Graph('DFS')
        v0 = g.addVertex('0', 0)
        v1 = g.addVertex('1', 0)
        v2 = g.addVertex('2', 0)
        v3 = g.addVertex('3', 0)
        v4 = g.addVertex('4', 4)
        v5 = g.addVertex('5', 0)
        v6 = g.addVertex('6', 0)
        v7 = g.addVertex('7', 0)
        v8 = g.addVertex('8', 0)

        g.addEdge('01', 4, v0, v1, directed=False)
        g.addEdge('07', 8, v0, v7, directed=False)
        g.addEdge('17', 11, v1, v7, directed=False)
        g.addEdge('12', 8, v1, v2, directed=False)
        g.addEdge('76', 1, v7, v6, directed=False)
        g.addEdge('78', 7, v7, v8, directed=False)
        g.addEdge('68', 6, v6, v8, directed=False)
        g.addEdge('28', 2, v8, v2, directed=False)
        g.addEdge('25', 4, v2, v5, directed=False)
        g.addEdge('65', 2, v6, v5, directed=False)
        g.addEdge('23', 7, v2, v3, directed=False)
        g.addEdge('35', 14, v5, v3, directed=False)
        g.addEdge('34', 9, v3, v4, directed=False)
        g.addEdge('54', 10, v4, v5, directed=False)
        dfs = g.DFS()
        actual = [vertex.name for vertex in dfs]
        expect = ['0', '1', '7', '6', '8', '2', '5', '3', '4']
        return self.assertEqual(actual, expect)

    def testDFS2(self):
        g = Graph('DFS')
        v0 = g.addVertex('0', 0)
        v1 = g.addVertex('1', 0)
        v2 = g.addVertex('2', 0)
        v3 = g.addVertex('3', 0)
        v4 = g.addVertex('4', 0)
        v5 = g.addVertex('5', 0)
        v6 = g.addVertex('6', 0)
        v7 = g.addVertex('7', 4)
        v8 = g.addVertex('8', 0)

        g.addEdge('01', 4, v0, v1, directed=False)
        g.addEdge('02', 8, v0, v2, directed=False)
        g.addEdge('03', 11, v0, v3, directed=False)
        g.addEdge('14', 8, v1, v4, directed=False)
        g.addEdge('25', 1, v2, v5, directed=False)
        g.addEdge('26', 7, v2, v6, directed=False)
        g.addEdge('37', 6, v3, v7, directed=False)
        g.addEdge('78', 2, v7, v8, directed=False)

        dfs = g.DFS()
        expect = [vertex.name for vertex in dfs]
        actual = ['0', '1', '4', '2', '5', '6', '3', '7', '8']

        return self.assertEqual(actual, expect)

    def testBFS2(self):
        g = Graph('DFS')
        v0 = g.addVertex('0', 0)
        v1 = g.addVertex('1', 0)
        v2 = g.addVertex('2', 0)
        v3 = g.addVertex('3', 0)
        v4 = g.addVertex('4', 0)
        v5 = g.addVertex('5', 0)
        v6 = g.addVertex('6', 0)
        v7 = g.addVertex('7', 4)
        v8 = g.addVertex('8', 0)

        g.addEdge('01', 4, v0, v1, directed=False)
        g.addEdge('02', 8, v0, v2, directed=False)
        g.addEdge('03', 11, v0, v3, directed=False)
        g.addEdge('14', 8, v4, v1, directed=False)
        g.addEdge('25', 1, v2, v5, directed=False)
        g.addEdge('26', 7, v2, v6, directed=False)
        g.addEdge('37', 6, v3, v7, directed=False)
        g.addEdge('78', 2, v7, v8, directed=False)

        bfs = g.BFS(v0)
        expect = [vertex.name for vertex in bfs]
        actual = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        return self.assertEqual(actual, expect)


class TestVertex(unittest.TestCase):

    def testCreateVertex(self):
        graph = Graph(name='name')
        v = Vertex(graph=graph, name='name', value=0)
        return self.assertIsInstance(v, Vertex)


class TestEdge(unittest.TestCase):
    def testCreateEdge(self):
        graph = Graph(name='name')
        v1 = Vertex(graph=graph, name='v1', value=0)
        v2 = Vertex(graph=graph, name='v2', value=0)
        e = Edge(name='ed', weight=4, from_vertex=v1, to_vertex=v2)
        return self.assertIsInstance(e, Edge)


if __name__ == '__main__':
    unittest.main()
