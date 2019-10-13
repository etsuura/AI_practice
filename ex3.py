import copy
from queue import PriorityQueue

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

def ucs(graph, start, goal):
    closed = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        print(queue.queue, closed)

        cost, node = queue.get()
        if node not in closed:
            closed.add(node)

            if node == goal:
                break
            for i in graph.neighbors(node):
                if i not in closed:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, i))

    print(queue.queue, closed)
    print("finish")

def BestFirstResearch(graph, start):
    openlist = [start]
    closedlist = []
    past_dict = {}
    pre_cost_dict = {}
    now_pre_cost = 0

    print("Best First Search")
    print("start")

    while len(openlist) != 0:           #step2
        print(openlist, closedlist)

        vertex = openlist.pop(0)        #step3
        closedlist.append(vertex)
        if len(pre_cost_dict) != 0:
            now_pre_cost = 0
            for i in range(len(past_dict)):
                a = past_dict[vertex]
                if len(a) >1:           #過去分を足す
                    for j in range(len(past_dict[vertex]) - 1):
                        now_pre_cost += pre_cost_dict[a[j + 1]]
                now_pre_cost += pre_cost_dict[vertex]   #今回の移動分を足す

        if (vertex == "G"):             #step4
            break

        path_list = graph[vertex]       #行き先とコストの取得
        for i in range(len(path_list)): #step5
            if (path_list[i][0] in closedlist) == False and (path_list[i][0] in openlist) == False:
                openlist.append(path_list[i][0])                #openlistに行き先追加
                pre_cost_dict[path_list[i][0]] = path_list[i][2] + now_pre_cost
                past_dict.setdefault(path_list[i][0], list(vertex))
                past_path = past_dict[path_list[i][0]]
                if vertex in past_path == False:
                    past_path.append(vertex)
                    past_dict[path_list[i][0]] = past_path

        openlist_cost = []              #make openlist_cost openlistとcostを対応付け
        for i in openlist:
            openlist_cost.append([i, pre_cost_dict[i]])

        #コスト順にソート
        openlist_cost = sorted(openlist_cost, key=lambda x: x[1])   #2番目の要素をもとにソート

        openlist = []
        for i in range(len(openlist_cost)):
            openlist.append(openlist_cost[i][0])

        past_path_list = graph[openlist[0]]

        # pastlist.append(openlist[0])

        path_list = []      #初期化

    print(openlist, closedlist)
    print("finish")

def A_asterisk (graph, start):
    openlist = [start]
    closedlist = []
    cost_dict = {}
    pre_cost_dict = {}
    old_sum_cost_dict = {}
    sum_cost_dict = {}   #sum = cost + pre_cost
    now_cost = 0
    now_pre_cost = 0

    print("A_asterisk")
    print("start")

    while len(openlist) != 0:       # step2
        print(openlist, closedlist)

        vertex = openlist.pop(0)    # step3
        closedlist.append(vertex)

        if (vertex == "G"):         # step4
            break

        path_list = graph[vertex]  # 行き先とコストの取得
        if len(pre_cost_dict) != 0:
            now_pre_cost += pre_cost_dict[vertex]

        #step5 calc f_hat(=sum_cost_dict)
        num = len(path_list)        #予測
        for i in range(num):
            pre_cost_dict[path_list[i][0]] = path_list[i][2] + now_pre_cost

        for i in range(num):        #コスト
            cost_dict.setdefault(path_list[i][0], path_list[i][1] + now_cost)
            if cost_dict[path_list[i][0]] > path_list[i][1] + now_cost:
                cost_dict[path_list[i][0]] = path_list[i][1] + now_cost

        for i in range(num):
            sum_cost_dict[path_list[i][0]] = pre_cost_dict[path_list[i][0]] + cost_dict[path_list[i][0]]
            if (path_list[i][0] in old_sum_cost_dict) == False:
                old_sum_cost_dict = copy.deepcopy(sum_cost_dict)

        # if len(old_sum_cost_dict) == 0:
        #     old_sum_cost_dict = copy.deepcopy(sum_cost_dict)


        #step6
        for i in range(len(path_list)):
            if (path_list[i][0] in closedlist) == False and (path_list[i][0] in openlist) == False:
                openlist.append(path_list[i][0])
                # cost_dict[path_list[i][0]] = path_list[i][1]

            if sum_cost_dict[path_list[i][0]] < old_sum_cost_dict[path_list[i][0]]:           #step7
                if path_list[i][0] in closedlist:
                    closedlist.remove(path_list[i][0])
                    openlist.append(path_list[i][0])
                    old_sum_cost_dict[path_list[i][0]] = sum_cost_dict[path_list[i][1]]
                elif path_list[i][0] in openlist:
                    old_sum_cost_dict[path_list[i][0]] = sum_cost_dict[path_list[i][1]]

        path = openlist

        # make openlist_cost
        openlist_cost = []
        for i in path:
            openlist_cost.append([i, old_sum_cost_dict[i]])

        # コスト順にソート
        openlist_cost = sorted(openlist_cost, key=lambda x: x[1])  # 2番目の要素をもとにソート

        openlist = []
        for i in range(len(openlist_cost)):
            openlist.append(openlist_cost[i][0])

        now_cost = cost_dict[openlist_cost[0][0]]
        path_list = []  # 初期化

    print(openlist, closedlist)
    print("finish")

def print_layout(text):
    print("__________________________________")
    print(text)

def main():
    # graph = {
    #     "S": list((("A", 1, 3), ("B", 3, 1), ("C", 5, 1))),
    #     "A": list((("S", 1, 4), ("D", 1, 3))),
    #     "B": list((("S", 3, 4), ("D", 2, 3), ("G", 1, 0))),
    #     "C": list((("S", 5, 4), ("G", 5, 0))),
    #     "D": list((("A", 1, 3), ("B", 2, 1), ("G", 5, 0))),
    #     "G": list((("B", 1, 1), ("C", 5, 1), ("D", 5, 3)))
    # }
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


    # print_layout("ex3_1")
    # OptimalSearch(graph, "S")
    print_layout("ex3_2")
    ucs(graph, "S", "G")
    # print_layout("ex3_3")
    # A_asterisk(graph, "S")

if __name__ == '__main__':
    main()