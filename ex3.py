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
        for i in range(len(path_list)):  #step5
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
        for i in range(len(path)):
            index = path[i]
            if cost_dir[index] > (now_cost + path_dir[index]):
                cost_dir[index] = now_cost + path_dir[index]

        openlist_cost = []
        for i in range(len(openlist)):
            index = openlist[i]
            openlist_cost.append([index, cost_dir[index]])

        #コスト順にソート
        sort_list = sorted(openlist_cost, key=lambda x: x[1])   #2番目の要素をもとにソート

        openlist = []
        for i in range(len(sort_list)):
            openlist.append(sort_list[i][0])

        openlist_cost = sort_list
        path_list = []      #初期化

    print(openlist, closedlist)
    print("finish")


def main():
    """
    graph = {
        "S": list(("A", "B")),
        "A": list(("S", "B", "C")),
        "B": list(("S", "A", "E", "F")),
        "C": list(("A", "E", "D")),
        "D": list(("C", "D", "G")),
        "E": list(("B", "C", "D", "G")),
        "F": list(("B")),
        "G": list(("D", "E"))
    }
    """

    graph = {
        "S": list((("A", 1), ("B", 3), ("C", 5))),
        "A": list((("S", 1), ("D", 1))),
        "B": list((("S", 3), ("D", 2), ("G", 1))),
        "C": list((("S", 5), ("G", 5))),
        "D": list((("A", 1), ("B", 2), ("G", 5))),
        "G": list((("B", 1), ("C", 5), ("D", 5)))
    }

    print("__________________________________")
    print("ex3_1")
    OptimalSearch(graph, "S")

if __name__ == '__main__':
    main()