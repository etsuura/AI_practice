def OptimalSearch(graph, start):
    openlist = [start]
    closedlist = []
    cost_dict = {}
    now_cost = 0

    print("Optimal Search")
    print("start")

    while len(openlist) != 0:           #step2
        print(openlist, closedlist)

        vertex = openlist.pop(0)        #step3
        closedlist.append(vertex)

        if (vertex == "G"):             #step4
            break

        path_list = graph[vertex]       #行き先とコストの取得

        for i in range(len(path_list)): #step5
            if (path_list[i][0] in closedlist) == False and (path_list[i][0] in openlist) == False:
                openlist.append(path_list[i][0])                #openlistに行き先追加
            cost_dict.setdefault(path_list[i][0], path_list[i][1] + now_cost)
            if cost_dict[path_list[i][0]] > path_list[i][1] + now_cost:
                cost_dict[path_list[i][0]] = path_list[i][1] + now_cost

        openlist_cost = []
        for i in openlist:  #openlistとコストの対応付け
            openlist_cost.append([i, cost_dict[i]])

        openlist_cost = sorted(openlist_cost, key=lambda x: x[1])   #2番目の要素をもとにソート

        openlist = []
        for i in range(len(openlist_cost)):     #ソート順に更新
            openlist.append(openlist_cost[i][0])

        now_cost = cost_dict[openlist_cost[0][0]]
        path_list = []      #初期化

    print(openlist, closedlist)
    print("finish")
    print("The cost was %d." %cost_dict["G"])

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

    print("ex3_2")
    OptimalSearch(graph, "S", "G")

if __name__ == '__main__':
    main()