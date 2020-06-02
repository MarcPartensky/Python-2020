class Graph:
    def __init__(self, vertices, edges):
        """Create a graph using its vertices and edges."""
        self.vertices = vertices  # list
        self.edges = edges  # dictionary

    def __str__(self):
        """Return the string representation of a graph."""
        return "Graph(vertices:" + str(self.vertices) + ",edges:" + str(self.edges) + ")"

    def getNodes(self):
        return self.vertices

    def setNodes(self, nodes):
        self.vertices = nodes

    nodes = property(getNodes, setNodes, "Nodes are vertices.")

    def append(self, vertex):
        self.vertices.append(vertex)

    def extend(self, vertices):
        self.vertices.extend(vertices)

    def __getitem__(self, key):
        return self.vertices[key]
    
    def __setitem__(self, key, value):
        self.vertices[key] = value

    def show(self, context):
        """Show the graph on the given context."""
        pass

    def connected(self):
        """Determine if the graph is connected."""
        # return

    def hamiltonian(self):
        """Determine if the graph is hamiltonian."""

    def eulerian(self):
        """Determine if the graph is eulerian."""

    def forest(self):
        """Determine if the graph is a forest."""

    def cyclomaticNumber(self):
        """Determine the number of linearly independent cycles."""

    @property
    def n(self):
        """Return the number of vertices."""
        return len(self.vertices)

    @property
    def e(self):
        """Return the number of edges."""
        return len(self.edges)

    @property
    def p(self):
        """Return the number of connected components."""
        # return len(self.)


class SimpleGraph(Graph):


class OrientedGraph(Graph):
    def getMatrix(self):
        a = []
        for i in range(self.n):
            self.edges[self.verticies[n]]
            b = []
            for j in range(self.n):
                if

class MultipleGraph(Graph):





if __name__ == "__main__":
    g = Graph("abc", [(1, 2)])
    print(g)
