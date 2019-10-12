import copy

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

        # path = []
        # path_dict = {}
        # for i in range(len(path_list)):     #再計算する項の取得
        #     if (path_list[i][0] in closedlist) == False:
        #         path.append(path_list[i][0])
        #         path_dict[path_list[i][0]] = path_list[i][1]

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

def BestFirstResearch(graph, start):
    openlist = [start]
    closedlist = []
    pre_cost_dict = {}
    pre_now_cost = 0

    print("Best First Search")
    print("start")

    while len(openlist) != 0:           #step2
        print(openlist, closedlist)

        vertex = openlist.pop(0)        #step3
        closedlist.append(vertex)
        if len(pre_cost_dict) != 0:
            pre_now_cost += pre_cost_dict[vertex]

        if (vertex == "G"):             #step4
            break

        path_list = graph[vertex]       #行き先とコストの取得
        for i in range(len(path_list)): #step5
            if (path_list[i][0] in closedlist) == False and (path_list[i][0] in openlist) == False:
                openlist.append(path_list[i][0])                #openlistに行き先追加
                pre_cost_dict[path_list[i][0]] = path_list[i][2] + pre_now_cost

        openlist_cost = []              #make openlist_cost openlistとcostを対応付け
        for i in openlist:
            openlist_cost.append([i, pre_cost_dict[i]])

        #コスト順にソート
        openlist_cost = sorted(openlist_cost, key=lambda x: x[1])   #2番目の要素をもとにソート

        openlist = []
        for i in range(len(openlist_cost)):
            openlist.append(openlist_cost[i][0])

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
    pre_now_cost = 0

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
            pre_now_cost += pre_cost_dict[vertex]

        #step5 calc f_hat(=sum_cost_dict)
        num = len(path_list)
        for i in range(num):
            pre_cost_dict[path_list[i][0]] = path_list[i][2] + pre_now_cost

        for i in range(num):        #修正
            cost_dict[path_list[i][0]] = path_list[i][1]

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
                cost_dict[path_list[i][0]] = path_list[i][1]
            else:     #step7
                if sum_cost_dict[path_list[i][0]] < old_sum_cost_dict[path_list[i][0]]:
                    closedlist.remove(path_list[i][0])
                    openlist.append(path_list[i][0])
                    old_sum_cost_dict[path_list[i][0]] = sum_cost_dict[path_list[i][1]]

        path = openlist

        # make openlist_cost
        openlist_cost = []
        for i in path:
            openlist_cost.append([i, sum_cost_dict[i]])

        # コスト順にソート
        openlist_cost = sorted(openlist_cost, key=lambda x: x[1])  # 2番目の要素をもとにソート

        openlist = []
        for i in range(len(openlist_cost)):
            openlist.append(openlist_cost[i][0])

        path_list = []  # 初期化

    print(openlist, closedlist)
    print("finish")

def print_layout(text):
    print("__________________________________")
    print(text)

def main():
    graph = {
        "S": list((("A", 1, 3), ("B", 3, 1), ("C", 5, 1))),
        "A": list((("S", 1, 4), ("D", 1, 3))),
        "B": list((("S", 3, 4), ("D", 2, 3), ("G", 1, 0))),
        "C": list((("S", 5, 4), ("G", 5, 0))),
        "D": list((("A", 1, 3), ("B", 2, 1), ("G", 5, 0))),
        "G": list((("B", 1, 1), ("C", 5, 1), ("D", 5, 3)))
    }

    print_layout("ex3_1")
    OptimalSearch(graph, "S")
    # print_layout("ex3_2")
    # BestFirstResearch(graph, "S")
    # print_layout("ex3_3")
    # A_asterisk(graph, "S")

if __name__ == '__main__':
    main()