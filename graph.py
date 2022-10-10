import numpy as np

class Node:
    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc # индекс в матрице смежности
    
    def __repr__(self):
        return self.data
    
class Graph:
    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)
    
    def __init__(self, row, col, nodes=None):
        self.adj_M = np.zeros(shape=(row, col)) # матрица смежности
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    def connect_unilateral(self, node1, node2, weight=1): # одностороннее соединение
        self.adj_M[node1.index][node2.index] = weight
    
    def disconnect_unilateral(self, node1, node2):
        self.adj_M[node1.index][node2.index] = 0
    
    def connect(self, node1, node2, weight=1): # двустороннее соединение
        self.connect_unilateral(node1, node2, weight)
        self.connect_unilateral(node2, node1, weight)

    def disconnect(self, node1, node2):
        self.disconnect_unilateral(node1, node2)
        self.disconnect_unilateral(node2, node1)

    def connections_from(self, node): # какие узлы указывают на данный узел
        connections = []
        for col in range(self.adj_M[node.index].shape[0]):
            if self.adj_M[node.index, col] != 0:
                connections.append((self.nodes[col], self.adj_M[node.index, col]))
        return connections
    
    def connections_to(self, node): # на какие узлы указывает данный узел
        connections = []
        for row in range(self.adj_M[:, node.index].shape[0]):
            if self.adj_M[row, node.index] != 0:
                connections.append((self.nodes[row], self.adj_M[row, node.index]))

    def is_connected(self, node1, node2):
        return self.adj_M[node1.index, node2.index] != 0 or self.adj_M[node2.index, node1.index] != 0
    
    def get_weight(self, node1, node2):
        return self.adj_M[node1.index, node2.index]

    def add_node(self, node):
        self.nodes.append(node)
        node.index = len(self.nodes)-1
        rows, cols = self.adj_M.shape
        new_adj_M = np.zeros(shape=(rows+1, cols+1))
        new_adj_M[:rows,:cols] = self.adj_M
        self.adj_M = new_adj_M
    
    def __repr__(self) -> str:
        return self.adj_M.__str__()

    def dijkstra(self, node):
        dist = [None] * len(self.nodes)
        # dist[0] - минимальное найденное расстояние пути, dist[1] - путь
        for i in range(len(dist)):
            # установим расстояние равное бесконечности до каждого узла
            dist[i] = [float('inf')]
            # перескок узла сам на себя
            dist[i].append([self.nodes[node.index]])
        
        # расстояние узла до самого себя равна 0
        dist[node.index][0] = 0
        # очередь на проверку
        queue = list(range(len(self.nodes)))
        # посещенные узлы
        seen = set()

        while len(queue) > 0: # пока очередь не пустая
            min_dist = float('inf')
            next_node_index = None
            
            # получение следующего узла для проверки
            for index in queue:
                if dist[index][0] < min_dist and index not in seen:
                    min_dist = dist[index][0]
                    next_node_index = index

            # проверка узла
            connections = self.connections_from(self.nodes[next_node_index])
            for (connected_node, weight) in connections:
                total_dist = weight + min_dist
                if total_dist < dist[connected_node.index][0]:
                    dist[connected_node.index][0] = total_dist
                    dist[connected_node.index][1] = list(dist[next_node_index][1])
                    dist[connected_node.index][1].append(connected_node)

            # добавление узла в увиденные и извлечение из очереди
            queue.remove(next_node_index)
            seen.add(next_node_index)
        
        return dist