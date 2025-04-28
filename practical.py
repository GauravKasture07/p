# from collections import deque
# def create_graph(edges):
#     graph={}
#     for edge in edges:
#         u,v=edge
#         if u in graph:
#             graph[u].append(v)
#         else:
#             graph[u]=[v]
#         if v in graph:
#             graph[v].append(u)
#         else:
#             graph[v]=[u]
#     return graph
# def bfs(graph,start,queue):
#     visited=set()
#     queue.append(start)
#     visited.add(start)
#     while queue:
#         node=queue.popleft()
#         print(node,end=" ")
#         if node in graph:
#             for neighbour in graph[node]:
#                 if neighbour not in visited:
#                     queue.append(neighbour)
#                     visited.add(neighbour)

# def dfs(graph,start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start, end=" ")
#     if start in graph:
#         for neighbour in graph[start]:
#             if neighbour not in visited:
#                 dfs(graph, neighbour, visited)
# def main():
#     num_vertices = int(input("Enter the number of vertices: "))
#     edges = []
#     num_edges = int(input("Enter the number of edges: "))
#     for i in range(num_edges):
#         u, v = map(int, input(f"Enter edge {i+1} (u v): ").split())
#         edges.append((u, v))
#     graph = create_graph(edges) 
#     print("Graph created:")
#     for node in graph:
#         print(node, ":", graph[node])
#     start_node_bfs = int(input("Enter the starting node for BFS: "))
#     print("BFS traversal:")
#     bfs(graph, start_node_bfs, deque())
# if __name__=="__main__":
#     main()


# def solve_n_queens(n):
#     def is_safe(board, row, col):
#         if any(board[i][col] == 1 for i in range(row)):
#             return False
#         for i in range(row):
#             if abs(row - i) == abs(col - board[i].index(1)) if 1 in board[i] else False:
#                 return False
#         return True
#     def solve_n_queens_util(board, row):
#         if row == n:
#             return True
#         for col in range(n):
#             if is_safe(board, row, col):
#                 board[row][col] = 1
#                 if solve_n_queens_util(board, row + 1):
#                     return True
#                 board[row][col] = 0
#         return False
#     board = [[0] * n for _ in range(n)]
#     if not solve_n_queens_util(board, 0):
#         print("Solution does not exist")
#         return False
#     print("One solution:")
#     for row in board:
#         print(*row)
#     return True
# solve_n_queens(5)




# def find(parent,i):
# 	if parent[i]==i:
# 		return i
# 	return find(parent,parent[i])
# def union(parent,rank,x,y):
# 	xroot=find(parent,x)
# 	yroot=find(parent,y)
# 	if rank[xroot]<rank[yroot]:
# 		parent[xroot]=yroot
# 	elif rank[xroot]>rank[yroot]:
# 		parent[yroot]=xroot
# 	else:
# 		parent[yroot]=xroot
# 		rank[xroot]+=1
# def krushkal(graph,num_vertices):
# 	result=[]
# 	i=0
# 	e=0
# 	graph=sorted(graph,key=lambda item:item[2])

# 	parent=[]
# 	rank=[]

# 	for node in range(num_vertices):
# 		parent.append(node)
# 		rank.append(0)
# 	while e<len(graph)-1 and i<len(graph):
# 		u,v,w=graph[i]
# 		i=i+1
# 		x=find(parent,u)
# 		y=find(parent,v)
# 		if x!=y:
# 			e=e+1
# 			result.append([u,v,w])
# 			union(parent,rank,x,y)	
# 	print("Krushkal algorithm")
# 	for u,v,w in result:
# 		print("%d-%d:%d"%(u,v,w))

# def prim(graph, V):
#     selected = [False] * V
#     no_edge = 0
#     selected[0] = True

#     print("Prim's MST:")
#     while (no_edge < V - 1):
#         minimum = float('inf')
#         x = 0
#         y = 0

#         for i in range(V):
#             if selected[i]:
#                 for j in range(V):
#                     if ((not selected[j]) and graph[i][j]):  
#                         if minimum > graph[i][j]:
#                             minimum = graph[i][j]
#                             x = i
#                             y = j
#         print("%d - %d: %d" % (x, y, graph[x][y]))
#         selected[y] = True
#         no_edge += 1

#  User input for Kruskal's
#num_edges=int(input("Enter the number of edges"))
# graph_krushkal=[]
# num_vertices=0

# print("Enter the edges (u,v,w):")
# for _ in range(num_edges):
# 	u,v,w=map(int,input().split())
# 	graph_krushkal.append([u,v,w])
# 	num_vertices=max(num_vertices,u,v)
# krushkal(graph_krushkal,num_vertices)

# kruskal(graph_kruskal)

# User input for Prim's
# V = int(input("Enter the number of vertices for Prim's graph: "))
# print("Enter the adjacency matrix (row by row, space-separated, 0 for no edge):")
# graph_prim = []
# for _ in range(V):
#     row = list(map(int, input().split()))
#     graph_prim.append(row)

# prim(graph_prim, V)

# Graph_nodes = {
#     'A': [('B', 6), ('F', 3)],
#     'B': [('C', 3), ('D', 2)],
#     'C': [('D', 1), ('E', 5)],
#     'D': [('C', 1), ('E', 8)],
#     'E': [('I', 5), ('J', 5)],
#     'F': [('G', 1),('H', 7)] ,
#     'G': [('I', 3)],
#     'H': [('I', 2)],
#     'I': [('E', 5), ('J', 3)],
# }

# def get_neighbors(v):
#     if v in Graph_nodes:
#         return Graph_nodes[v]
#     else:
#         return None
        
# def h(n):
#         H_dist = {
#             'A': 10,
#             'B': 8,
#             'C': 5,
#             'D': 7,
#             'E': 3,
#             'F': 6,
#             'G': 5,
#             'H': 3,
#             'I': 1,
#             'J': 0             
#         }
#         return H_dist[n]
        
# def aStarAlgo(start_node, stop_node):         
#         open_set = set(start_node) 
#         closed_set = set()
#         g = {} 
#         parents = {}
#         g[start_node] = 0
#         parents[start_node] = start_node        
#         while len(open_set) > 0:
#             n = None
#             for v in open_set:
#                 if n == None or g[v] + h(v) < g[n] + h(n):
#                     n = v     
#             if n == stop_node or Graph_nodes[n] == None:
#                 pass
#             else:
#                 for (m, weight) in get_neighbors(n):
#                     if m not in open_set and m not in closed_set:
#                         open_set.add(m)
#                         parents[m] = n
#                         g[m] = g[n] + weight                         
#                     else:
#                         if g[m] > g[n] + weight:
#                             g[m] = g[n] + weight
#                             parents[m] = n
#                             if m in closed_set:
#                                 closed_set.remove(m)
#                                 open_set.add(m)
#             if n == stop_node:
#                 path = [] 
#                 while parents[n] != n:
#                     path.append(n)
#                     n = parents[n] 
#                 path.append(start_node)
#                 path.reverse()
#                 print('Path found: {}'.format(path))
#                 return path
#             open_set.remove(n)
#             closed_set.add(n) 
#         print('Path does not exist!')
#         return None
# aStarAlgo('A', 'J')



# def chatbot():
#     print("Welcome to the Customer Support Chatbot!")
#     print("How can I help you today?")

#     while True:
#         user_input = input("> ").lower()

#         if "hello" in user_input or "hi" in user_input:
#             print("Hello! How can I assist you?")
#         elif "goodbye" in user_input or "bye" in user_input:
#             print("Goodbye! Have a great day!")
#             break
#         elif "help" in user_input:
#             print("I can answer questions about orders, shipping, and returns.")
#         elif "order" in user_input:
#             print("To inquire about your order, please provide your order number.")
#         elif "shipping" in user_input:
#             print("Our standard shipping takes 5-7 business days.")
#         elif "return" in user_input:
#             print("You can initiate a return within 30 days of purchase.")
#         else:
#             print("I'm sorry, I don't understand. Please type 'help' for assistance.")

# if __name__ == "__main__":
#     chatbot()