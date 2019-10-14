def OptimalSearch(graph, start, goal):
    openlist = [start]
    closedlist = []
    cost_dict = {}
    now_cost = 0

    print("start")

    while len(openlist) != 0:           #step2
        print(openlist, closedlist)
        vertex = openlist.pop(0)        #step3
        closedlist.append(vertex)
        if vertex == goal:              #step4
            break
        for i in graph.neighbors(vertex):           #step5
            if i not in closedlist and i not in openlist:
                openlist.append(i)
            cost_dict.setdefault(i, graph.get_cost(vertex, i) + now_cost)
            if cost_dict[i] > graph.get_cost(vertex, i) + now_cost:
                cost_dict[i] = graph.get_cost(vertex, i) + now_cost

        openlist_cost = []
        for i in openlist:
            openlist_cost.append([i, cost_dict[i]])
        openlist_cost = sorted(openlist_cost, key=lambda x: x[1])   #2番目の要素をもとにソート

        openlist = []
        for i in range(len(openlist_cost)):
            openlist.append(openlist_cost[i][0])

        now_cost = cost_dict[openlist_cost[0][0]]

    print(openlist, closedlist)
    print("finish")

    print("The cost was %d." %cost_dict[goal])

class Graph:
    def __init__(self):
        self.edges = {}
        self.cost = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.cost[(from_node + to_node)]

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
        "BS": 4, "BD": 3, "BG": 0,
        "CS": 4, "CG": 0,
        "DA": 3, "DB": 1, "DG": 0,
        "GB": 1, "GC": 1, "GD": 3
    }

    print("ex3_1")
    OptimalSearch(graph, "S", "G")

if __name__ == '__main__':
    main()