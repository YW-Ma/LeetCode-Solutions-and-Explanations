''' TO DO: Find the shortest path from the source node to every other node in the given graph '''
'''
Dijkstra算法：

1. 一共用了哪几个数据结构？作用是什么？
result：一个字典，记录了到每个节点的最短路径的距离（当前）
path：一个字典，记录到除了源点的每个节点的最短路径的倒数第二个节点是什么（当前）
unvisited：一个set，存了尚未访问的节点（访问完会pop掉）


2. 更新的策略是什么？
初始化：
源点result是0，源点的neighbors的result是到源点的距离，其他点的result是infinity
path不用管，但是要声明是dict，以后修改的时候直接赋值就好。（不需要defaultdict）
unvisited要把所有尚未访问的节点都添加进去。

循环更新：
每次在unvisited的节点中，选择result最小的节点（A)
计算该节点（A）的result + 该节点（A）到其neighbors的distance 是否小于neighbors的result
如果小，就更新那个neighbor的result，和path中的节点
从unvisited set中移除节点（A）

输出结果：
在path中找到目标节点的上一个节点，
继续在path中找到上一个节点的上一个节点，
直到path里面不存在这个节点（即到了源点，源点只包含在value里，不包含在path的key里面）

3. 注意如何使用Graph类：
.nodes是一个set
.neighbours是一个defaultdict，以节点为key，以neighbours的列表为value
.distances是一个dict，以一个节点对为key('A', 'B')，以一个距离值为value

'''
import sys

# Helper Code
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}                  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    # lets make the graph undirected / bidirectional 
        
    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)

def dijkstra(graph, source):
    # Declare and initialize result, unvisited, and path
    result = dict()
    path = dict()
    unvisited = graph.nodes
    unvisited.remove(source)
    result[source] = 0
    for node in unvisited:
        if source in graph.neighbours[node]:
            result[node] = graph.distances[(node, source)]
        else:
            result[node] = sys.maxsize
    
    # As long as unvisited is non-empty
    while unvisited: 
        
        # 1. Find the unvisited node having smallest known distance from the source node.
        min_node = None
        min_value = sys.maxsize
        for node in unvisited:
            if min_value >= result[node]:
                min_value = result[node]
                min_node = node
        if min_node is None:
            return
        # 2. For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.
        current_node = min_node
        current_distance = min_value
        for node in graph.neighbours[current_node]:
            if node in unvisited:
                new_distance = current_distance + graph.distances[(current_node, node)]
                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.        
                # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                if new_distance < result[node]:
                    result[node] = new_distance
                    path[node] = current_node
        # 5. Remove the current node from the unvisited set.
        unvisited.remove(current_node)
        
    return result


# Test
# Test 1
graph_1 = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    graph_1.add_node(node)

graph_1.add_edge('A','B',3)
graph_1.add_edge('A','D',2)
graph_1.add_edge('B','D',4)
graph_1.add_edge('B','E',6)
graph_1.add_edge('B','C',1)
graph_1.add_edge('C','E',2)
graph_1.add_edge('E','D',1)

print(dijkstra(graph_1, 'A'))     # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}

# Test 2
graph_2 = Graph()
for node in ['A', 'B', 'C']:
    graph_2.add_node(node)
    
graph_2.add_edge('A', 'B', 5)
graph_2.add_edge('B', 'C', 5)
graph_2.add_edge('A', 'C', 10)

print(dijkstra(graph_2, 'A'))        # {'A': 0, 'C': 10, 'B': 5}

# Test 3
graph_3 = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph_3.add_node(node)
    
graph_3.add_edge('A', 'B', 5)
graph_3.add_edge('A', 'C', 4)
graph_3.add_edge('D', 'C', 1)
graph_3.add_edge('B', 'C', 2)
graph_3.add_edge('A', 'D', 2)
graph_3.add_edge('B', 'F', 2)
graph_3.add_edge('C', 'F', 3)
graph_3.add_edge('E', 'F', 2)
graph_3.add_edge('C', 'E', 1)

print(dijkstra(graph_3, 'A'))       # {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}