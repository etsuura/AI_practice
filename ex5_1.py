# ex5_1
# def main(n, cost):
#     dp = [0]*(n+1)
#     for i in range(n):
#         dp[i+1] = max(dp[i], dp[i] + cost[i])
#     print(dp[-1])

def DynamicProgramming(graph, start, goal):
    dp = [0] * len(graph.text)
    dict_keys = list(graph.text.keys())
    max_index = []

    graph.cost_memory[start] = [0, "0"]
    for i in range(len(graph.text) - 1):
        vertex = dict_keys[i]
        cost = []
        index_list = graph.neighbors(vertex)
        for index in index_list:
            cost.append(graph.cost[(vertex + index)])
        dp[i + 1] = dp[i] + max(cost)
        max_index.append(index_list[cost.index(max(cost))])
        graph.cost_memory[max_index[i]] = [dp[i+1], vertex]
    print(graph.cost_memory)

    print("MaxCost is %d" %graph.cost_memory["Goal"][0])


class Graph:
    def __init__(self):
        self.edges = {}
        self.cost = {}
        self.cost_memory = {}
        self.text = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.cost[(from_node + to_node)]

def main():
    graph = Graph()
    graph.edges = {
        "Start": ["A", "B", "C"],
        "A": ["D"],
        "B": ["D", "E", "F"],
        "C": ["E"],
        "D": ["G"],
        "E": ["G", "H", "I"],
        "F": ["H"],
        "G": ["J"],
        "H": ["J", "K", "L"],
        "I": ["K"],
        "J": ["Goal"],
        "K": ["Goal"],
        "L": ["Goal"],
        "Goal": []
    }
    graph.cost = {
        "StartA": 2, "StartB": 5, "StartC": 4,
        "AD": -5,
        "BD": 3, "BE": 2, "BF": 3,
        "CE": 5,
        "DG": 2,
        "EG": 2, "EH": -2, "EI": 1,
        "FH": 4,
        "GJ": 4,
        "HJ": 4, "HK": 2, "HL": 7,
        "IK": 0,
        "JGoal": 2,
        "KGoal": 1, "LGoal": 8
    }
    graph.cost_memory = {}
    graph.text = {
        "Start": "り",
        "A": "ん", "B": "つ", "C": "ば",
        "D": "め", "E": "い", "F": "う",
        "G": "い", "H": "あ", "I": "い",
        "J": "か", "K": "と", "L": "さ",
        "Goal": "ん"
    }

    print("ex5_1")
    DynamicProgramming(graph, "Start", "Goal")

if __name__ == '__main__':
    main()