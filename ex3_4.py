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

    path = []
    path.append(goal)
    current_node = goal
    while current_node != start:
        for i in graph.neighbors(current_node):
            if i in closedlist:
                path.insert(0, i)
                current_node = i
                closedlist.remove(i)
                break

    print("The shortest route is %s." %str(path))
    print("The cost was %d." %allcost.g[goal])

    # return path[::-1]

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
        "S": list(("3")),
        "1": list(("4")),
        "2": list(("6")),
        "3": list(("S", "4", "7")),
        "4": list(("1", "3", "6")),
        "5": list(("8")),
        "6": list(("4", "G")),
        "7": list(("3", "8", "9")),
        "8": list(("5", "7", "10")),
        "9": list(("7")),
        "10": list(("8")),
        "G": list(("6"))
    }
    graph.cost = {
        "S3": 2,
        "14": 3,
        "26": 2,
        "3S": 2, "34": 3, "37": 3,
        "41": 3, "43": 3, "46": 2,
        "58": 2,
        "64": 2, "6G": 5,
        "73": 3, "78": 1, "79": 2,
        "85": 2, "87": 1, "810": 1,
        "97": 2,
        "108": 1,
        "G6": 5
    }
    graph.weights = {
        "S3": 8,
        "14": 5,
        "26": 3,
        "3S": 10, "34": 5, "37": 5,
        "41": 8, "43": 8, "46": 3,
        "58": 4,
        "64": 5, "6G": 0,
        "73": 8, "78": 4, "79": 5,
        "85": 6, "87": 5, "810": 3,
        "97": 5,
        "108": 4,
        "G6": 3
    }

    print("ex3_3")
    AStarSearch(graph, "S", "G")

if __name__ == '__main__':
    main()