import heapq

# ダイクストラ法によって最短経路問題を解く
def solve_by_dijkstra(graph):
    # ノード毎のSTARTからの最大コスト
    max_dist_dict = {}
    # ノードに最大コストで辿り着く場合の直前のノード
    prev_node_dict = {}
    q = []
    heapq.heappush(q, (0, 'START'))
    prev_node_dict["START"] = ''
    max_dist_dict["START"] = 0
    while True:
        # 確定したノードから遷移可能なノードのうち
        # 最大のコストと遷移先ノードをmax_dist_dictとprev_node_dictに設定
        dist, node = heapq.heappop(q)
        # max_dist_dict[node] = dist
        # prev_node_dict[node] = prev_node
        # もしGOALノードの最大コストが確定したらループを抜ける
        if node == 'GOAL':
            return max_dist_dict, prev_node_dict
        # prev_node = node
        # 確定したノードから遷移可能なノードについて
        # コストを計算し，キュー(q)に追加する
        culc_max_dist_and_put(graph, q, node, max_dist_dict, prev_node_dict)


def culc_max_dist_and_put(graph, q, departure_node, max_dist_dict, prev_node_dict):
    # 直前に確定したノードから遷移可能なすべてのノードについて繰り返し
    for arrival_node in graph.neighbors(departure_node):
        # 遷移可能なノードについて，直前に確定したノードから遷移した場合のコストを計算
        tmp_d = max_dist_dict[departure_node] + graph.get_cost(departure_node, arrival_node)
        # 過去に遷移先ノードの最大コストを計算済みかどうか
        if arrival_node in max_dist_dict.keys():
            # 過去に計算していたSTARTからの最大コストより直前に確定したノードから遷移した場合の
            # コストが小さかった場合，最大コストを更新
            if tmp_d > max_dist_dict[arrival_node]:
                max_dist_dict[arrival_node] = tmp_d
                heapq.heappush(q, (max_dist_dict[arrival_node], arrival_node))
                prev_node_dict[arrival_node] = departure_node
        else:
            max_dist_dict[arrival_node] = tmp_d
            heapq.heappush(q, (max_dist_dict[arrival_node], arrival_node))
            prev_node_dict[arrival_node] = departure_node

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
    graph.cost_memory = {}
    graph.text = {
        "START": "り",
        "A": "ん", "B": "つ", "C": "ば",
        "D": "め", "E": "い", "F": "う",
        "G": "い", "H": "あ", "I": "い",
        "J": "か", "K": "と", "L": "さ",
        "GOAL": "ん"
    }

    max_dist_dict, prev_node_dict = solve_by_dijkstra(graph)
    # GOALノードからprev_node_dictをたどって経路を復元
    print('Route : GOAL ', end='')
    node = 'GOAL'
    while True:
        if node == 'START':
            print()
            break
        print(' ← ' + prev_node_dict[node], end='')
        node = prev_node_dict[node]
        #	⇒Route : GOAL  ← c ← a ← b ← START
    print('max Cost : ' + str(max_dist_dict['GOAL']))

if __name__ == '__main__':
    main()