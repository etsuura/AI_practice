#人工知能概論練習課題

def depthFirstSearch(graph, start):
    openlist = [start]
    closedlist = []     #step1

    print("depth first search")
    print("start")
    while len(openlist) != 0:   #step2
        print(openlist, closedlist)
        vertex = openlist.pop(0)
        if (vertex == "G"):     #step3
            closedlist.append(vertex)
            break
        closedlist.append(vertex)   #step4
        path = graph[vertex]
        for i in range(len(path)):  #step5
            if (path[i] in closedlist) == False and (path[i] in openlist) == False:
                openlist.insert(0, path[i])
        path = []

    print(openlist, closedlist)
    print("finish")

def breadthFirstSearch(graph, start):
    openlist = [start]
    closedlist = []     #step1

    print("breadth first search")
    print("start")
    while len(openlist) != 0:   #step2
        print(openlist, closedlist)
        vertex = openlist.pop(0)
        if (vertex == "G"):     #step3
            closedlist.append(vertex)
            break
        closedlist.append(vertex)
        path = graph[vertex]  #step4
        for i in range(len(path)):
            if (path[i] in closedlist) == False and (path[i] in openlist) == False:
                openlist.append(path[i])
        path = []

    print(openlist, closedlist)
    print("finish")

def ex2_4(method):
    graph = {
        "S": list(("3")),
        "1": list(("4")),
        "2": list(("6")),
        "3": list(("S", "4", "7")),
        "4": list(("1", "3", "6")),
        "5": list(("8")),
        "6": list(("2", "4", "G")),
        "7": list(("3", "8", "9")),
        "8": list(("5", "7", "10")),
        "9": list(("7")),
        "10": list(("8")),
        "G": list(("6"))
    }

    if (method == "dfs"):
        depthFirstSearch(graph, "S")
    elif(method == "bfs"):
        breadthFirstSearch(graph, "S")
    else:
        print("else")

def main():
    graph = {
        "S": list(("A", "B")),
        "A": list(("S", "C", "D")),
        "B": list(("S", "C")),
        "C": list(("A", "B", "D")),
        "D": list(("A", "C"))
    }

    print("__________________________________")
    print("ex2_2")
    depthFirstSearch(graph, "S")
    print("__________________________________")

    print("ex2_3")
    breadthFirstSearch(graph, "S")
    print("__________________________________")

    print("ex2_4")
    ex2_4("dfs")
    print("__________________________________")

    ex2_4("bfs")
    print("__________________________________")

if __name__ == "__main__":
    main()