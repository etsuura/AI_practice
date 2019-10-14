import copy
from queue import PriorityQueue

def AStarSearch(graph, start, goal):
    openlist = [start]
    closedlist = []
    queue = PriorityQueue()
    queue.put((0, start))
    allcost = cost_class()
    now_cost = 0

    print("start")

    while openlist != 0:                #step2
        print(openlist, closedlist)
        cost_list = []

        cost, _ = queue.get()
        node = openlist.pop(0)          #step3
        if node not in closedlist:
            closedlist.append(node)
            if node == goal:            #step4
                break
            for i in graph.neighbors(node):     #step5
                if i not in closedlist:
                    total_cost = cost + graph.get_weight(node, i)
                    allcost.set_h(i, total_cost)    #set_h
                    queue.put((total_cost, i))
                else:
                    allcost.h.setdefault(i, 0)

                allcost.g.setdefault(i, graph.get_cost(node, i) + now_cost)
                if allcost.g[i] > graph.get_cost(node, i) + now_cost:
                    allcost.g[i] = graph.get_cost(node, i) + now_cost   #set_g

                if (i not in closedlist) and (i not in openlist):   #step6
                    openlist.append(i)
                    allcost.set_f(i)
                    allcost.copy_f(i)
                elif i in closedlist:   #step7
                    if i not in allcost.f:
                        allcost.set_f(i)
                    if i not in allcost.old_f:
                        allcost.copy_f(i)
                    if allcost.get_f(i) < allcost.get_old_f(i):
                        allcost.copy_f(i)
                        closedlist.remove(i)
                        openlist(i)
                else:
                    if i not in allcost.f:
                        allcost.set_f(i)
                    if i not in allcost.old_f:
                        allcost.copy_f(i)
                    if allcost.get_f(i) < allcost.get_old_f(i):
                        allcost.copy_f(i)

            for i in openlist:
                    cost_list.append((i, allcost.get_old_f(i)))

            cost_list = sorted(cost_list, key=lambda x: x[1])  # 2番目の要素をもとにソート
            openlist = []
            for i in range(len(cost_list)):
                openlist.append(cost_list[i][0])

            now_cost = allcost.g[cost_list[0][0]]

    print(openlist, closedlist)
    print("finish")
    print("The cost was %d." %allcost.g[goal])

class cost_class:
    def __init__(self):
        self.g = {}
        self.h = {}
        self.f = {}
        self.old_f = {}
    def set_g(self, node, value):
        self.g[node] = value

    def set_h(self, node, value):
        self.h[node] = value

    def set_f(self, node):
        self.f[node] = self.g[node] + self.h[node]

    def get_f(self, node):
        return self.f[node]

    def copy_f(self, node):
        self.old_f[node] = copy.deepcopy(self.f[node])

    def get_old_f(self, node):
        return self.old_f[node]

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

    print("ex3_3")
    AStarSearch(graph, "S", "G")

if __name__ == '__main__':
    main()