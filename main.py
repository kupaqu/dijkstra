from graph import Node, Graph

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n4 = Node("4")
n5 = Node("5")
n6 = Node("6")
n7 = Node("7")
n8 = Node("8")
n9 = Node("9")


w_graph = Graph.create_from_nodes([n1,n2,n3,n4,n5,n6,n7,n8,n9])
 
w_graph.connect_unilateral(n1, n2, 10)
w_graph.connect_unilateral(n1, n4, 8)
w_graph.connect_unilateral(n1, n3, 6)

w_graph.connect_unilateral(n2, n4, 5)
w_graph.connect_unilateral(n2, n7, 11)

w_graph.connect_unilateral(n3, n5, 3)

w_graph.connect_unilateral(n4, n5, 5)
w_graph.connect_unilateral(n4, n6, 7)
w_graph.connect_unilateral(n4, n7, 12)

w_graph.connect_unilateral(n5, n6, 9)
w_graph.connect_unilateral(n5, n9, 12)

w_graph.connect_unilateral(n6, n8, 8)
w_graph.connect_unilateral(n6, n9, 10)

w_graph.connect_unilateral(n7, n6, 4)
w_graph.connect_unilateral(n7, n8, 6)

w_graph.connect_unilateral(n8, n9, 15)
 
print(w_graph.dijkstra(n1))