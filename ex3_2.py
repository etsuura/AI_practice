from queue import PriorityQueue

def ucs(graph, start, goal):
    openlist = [start]
    closedlist = []

    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    print("start")

    while queue:
        print(openlist, closedlist)

        cost, node = queue.get()
        if node not in closedlist:      #step2
            openlist.remove(node)       #step3
            closedlist.append(node)
            if node == goal:            #step4
                break
            for i in graph.neighbors(node):     #step5
                if i not in closedlist:
                    total_cost = cost + graph.get_weight(node, i)
                    queue.put((total_cost, i))
                    if i not in closedlist and i not in openlist:
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

    def get_weight(self, from_node, to_node):
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
    graph.cost = {
        "SA": 1, "SB": 3, "SC": 5,
        "AS": 1, "AD": 1,
        "BS": 3, "BD": 2, "BG": 1,
        "CS": 5, "CG": 5,
        "DA": 2, "DB": 3, "DG": 5,
        "GB": 1, "GC": 5, "GD": 5
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