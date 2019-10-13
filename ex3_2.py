from queue import PriorityQueue

def ucs(graph, start, goal):
    openlist = [start]
    closedlist = []

    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        print(openlist, closedlist)

        cost, node = queue.get()
        if node not in visited:
            visited.add(node)
            openlist.remove(node)
            closedlist.append(node)
            if node == goal:

                break
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))
                    if (i in closedlist) == False and (i in openlist) == False:
                        openlist.append(i)

    print(openlist, closedlist)
    print("finish")

class Graph:
    def __init__(self):
        self.edges = {}
        self.cost = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]

def main():
    graph = Graph()
    graph.edges = {
        "S": list(("A", "B", "C")),
        "A": list(("S", "D")),
        "B": list(("S", "D", "G")),
        "C": list(("S", "G")),
        "D": list(("A", "B", "G")),
        "G": list(("B", "C", "D"))
    }
    graph.weights = {
        "SA": 3, "SB": 1, "SC": 1,
        "AS": 4, "AD": 3,
        "BA": 4, "BD": 3, "BG": 0,
        "CA": 4, "CG": 0,
        "DA": 3, "DB": 1, "DG": 0,
        "GB": 1, "GC": 1, "GD": 3
    }

    print("ex3_2")
    ucs(graph, "S", "G")

if __name__ == '__main__':
    main()