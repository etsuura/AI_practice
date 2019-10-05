#人工知能概論練習課題

graph = {
"S" : list(("A" ,"B")),
"A" : list(("S", "C", "D")),
"B" : list(("S", "C")),
"C" : list(("A", "B", "D")),
"D" : list(("A", "C"))}

def depthFirstSearch(graph, start):
    openlist = [start]
    closedlist = []     #step1

    print("depth first search")
    print("start")
    while len(openlist) != 0:   #step2
        print(openlist, closedlist)
        vertex = openlist.pop(0)
        closedlist.append(vertex)   #step3
        path = graph[vertex]  #step4
        for i in range(len(path)):
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
        closedlist.append(vertex)   #step3
        path = graph[vertex]  #step4
        for i in range(len(path)):
            if (path[i] in closedlist) == False and (path[i] in openlist) == False:
                openlist.append(path[i])
        path = []

    print(openlist, closedlist)
    print("finish")

def main():
    depthFirstSearch(graph, "S")
    breadthFirstSearch(graph, "S")
    #print(path)

if __name__ == "__main__":
    main()