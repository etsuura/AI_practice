def OptimalSearch(graph, start):
    openlist = [start]
    closedlist = []
    cost_dir = {}
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
                cost_dir[path_list[i][0]] = path_list[i][1]

        #再計算する項の取得
        path = []
        path_dir = {}
        for i in range(len(path_list)):
            if (path_list[i][0] in closedlist) == False:
                path.append(path_list[i][0])
                path_dir[path_list[i][0]] = path_list[i][1]

        #再計算
        for i in path:
            if cost_dir[i] > (now_cost + path_dir[i]):
                cost_dir[i] = now_cost + path_dir[i]

        #make openlist_cost
        openlist_cost = []
        for i in openlist:
            openlist_cost.append([i, cost_dir[i]])

        #コスト順にソート
        sort_list = sorted(openlist_cost, key=lambda x: x[1])   #2番目の要素をもとにソート

        openlist = []
        for i in range(len(sort_list)):
            openlist.append(sort_list[i][0])

        openlist_cost = sort_list
        path_list = []      #初期化

    print(openlist, closedlist)
    print("finish")

def BestFirstResearch(graph, start):
    openlist = [start]
    closedlist = []
    pre_cost_dir = {}

    print("Best First Search")
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
                pre_cost_dir[path_list[i][0]] = path_list[i][2]

        #再計算する項の取得
        path = []
        path_dir = {}
        for i in range(len(path_list)):
            if (path_list[i][0] in closedlist) == False:
                path.append(path_list[i][0])
                path_dir[path_list[i][0]] = path_list[i][2]

        #再計算
        # for i in path:
        #     if pre_cost_dir[i] > (now_cost + path_dir[i]):
        #         pre_cost_dir[i] = now_cost + path_dir[i]

        #make openlist_cost
        openlist_cost = []
        for i in openlist:
            openlist_cost.append([i, pre_cost_dir[i]])

        #コスト順にソート
        sort_list = sorted(openlist_cost, key=lambda x: x[1])   #2番目の要素をもとにソート

        openlist = []
        for i in range(len(sort_list)):
            openlist.append(sort_list[i][0])

        openlist_cost = sort_list
        path_list = []      #初期化

    print(openlist, closedlist)
    print("finish")



def print_layout(text):
    print("__________________________________")
    print(text)

def main():
    # graph = {
    #     "S": list((("A", 1), ("B", 3), ("C", 5))),
    #     "A": list((("S", 1), ("D", 1))),
    #     "B": list((("S", 3), ("D", 2), ("G", 1))),
    #     "C": list((("S", 5), ("G", 5))),
    #     "D": list((("A", 1), ("B", 2), ("G", 5))),
    #     "G": list((("B", 1), ("C", 5), ("D", 5)))
    # }

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
    print_layout("ex3_2")
    BestFirstResearch(graph, "S")

if __name__ == '__main__':
    main()