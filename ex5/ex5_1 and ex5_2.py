# ex5_1
def DynamicProgramming(graph, start, goal):
    print("Start")

    graph.cost_memory[start] = 0
    for time in graph.time.keys():
        for vertex in graph.time[time]:
            if vertex == goal:
                break
            for node in graph.neighbors(vertex):
                cost = graph.cost_memory[vertex] + graph.get_cost(vertex, node)
                if node not in graph.cost_memory.keys():
                    graph.cost_memory[node] = cost
                    graph.route[node] = vertex
                elif cost > graph.cost_memory[node]:
                    graph.cost_memory[node] = cost
                    graph.route[node] = vertex

    history = []
    node = goal
    while 1:
        history.append(node)
        if node == start:
            break
        node = graph.route[node]
    texts = history[::-1]
    for i in texts:
        print(graph.text[i], end="")
    print("")
    print("最大コストは%dです." %graph.cost_memory[goal])
    print("Finish")

    print("-------------------")
    print("ex5_2")
    print("Ft")
    print(graph.cost_memory)
    print("")
    print("st*")
    print(graph.route)

class Graph:
    def __init__(self):
        self.edges = {}
        self.cost = {}
        self.cost_memory = {}
        self.text = {}
        self.time = {}
        self.route = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.cost[(from_node + to_node)]

def main():
    graph = Graph()
    graph.edges = {
        "START": ["A", "B", "C"],
        "A": ["D"],
        "B": ["D", "E", "F"],
        "C": ["E"],
        "D": ["G"],
        "E": ["G", "H", "I"],
        "F": ["H"],
        "G": ["J"],
        "H": ["J", "K", "L"],
        "I": ["K"],
        "J": ["GOAL"],
        "K": ["GOAL"],
        "L": ["GOAL"],
        "GOAL": []
    }
    graph.cost = {
        "STARTA": 2, "STARTB": 5, "STARTC": 4,
        "AD": -5,
        "BD": 3, "BE": 2, "BF": 3,
        "CE": 5,
        "DG": 2,
        "EG": 2, "EH": -2, "EI": 2,
        "FH": 0,
        "GJ": 4,
        "HJ": 4, "HK": 2, "HL": 7,
        "IK": 0,
        "JGOAL": 2, "KGOAL": 1, "LGOAL": 8
    }
    graph.text = {
        "START": "り",
        "A": "ん", "B": "つ", "C": "ば",
        "D": "め", "E": "い", "F": "う",
        "G": "い", "H": "あ", "I": "い",
        "J": "か", "K": "と", "L": "さ",
        "GOAL": "ん"
    }
    graph.time = {
        "t0": ["START"],
        "t1": ["A", "B", "C"],
        "t2": ["D", "E", "F"],
        "t3": ["G", "H", "I"],
        "t4": ["J", "K", "L"],
        "T": ["GOAL"]
    }

    print("ex5_1")
    DynamicProgramming(graph, "START", "GOAL")

if __name__ == '__main__':
    main()