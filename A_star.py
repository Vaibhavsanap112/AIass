#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx


import heapq
graph={'A':[('B',6),('F',3)],'B':[('C',3),('D',2)],'C':[('E',5)],
       'D':[('E',8)],'E':[('J',3)],'F':[('G',4),('H',7)],
       'G':[('I',2),('J',5)],'H':[('I',2)],'I':[('J',1)],'J':[]}
h={'A':9,'B':8,'C':5,'D':7,'E':3,'F':6,'G':5,'H':3,'I':1,'J':0}

def a_star(start,goal):
    pq=[(h[start],0,[start])]
    while pq:
        f,g,path=heapq.heappop(pq)
        node=path[-1]
        if node==goal: return path,g
        for n,c in graph[node]:
            heapq.heappush(pq,(g+c+h[n],g+c,path+[n]))
    return [],float('inf')

s=input("Start node: "); g=input("Goal node: ")
p,c=a_star(s,g)
print("Path:",' → '.join(p))
print("Cost:",c)

# Input:
# Start node: A
# Goal node: J

# Output:
# Path: A → F → G → I → J
# Cost: 10

# ------------------------------------------------------
# EXPLANATION OF THE CODE (A* SEARCH ALGORITHM)
# ------------------------------------------------------

# 📘 AIM:
# This program implements the **A* (A-star) search algorithm**
# to find the shortest and most efficient path between a 
# start node and a goal node in a given graph.

# ------------------------------------------------------
# 📍 WHAT IS A* ALGORITHM?
# ------------------------------------------------------
# A* is a pathfinding algorithm that finds the shortest path
# between two nodes using both:
#   1. Actual cost (g) from the start node
#   2. Heuristic cost (h) — estimated distance to the goal
# It chooses the path that minimizes:
#   f(n) = g(n) + h(n)
# where:
#   f(n) → total estimated cost of the path through node n
#   g(n) → cost from start to node n
#   h(n) → estimated cost from node n to goal (heuristic)

# ------------------------------------------------------
# 🧩 CODE EXPLANATION (LINE BY LINE)
# ------------------------------------------------------

# import heapq
# → Imports the 'heapq' library which is used to create a priority queue.
#   This helps in efficiently getting the next node with the smallest cost.

# graph = {...}
# → Defines the graph as a dictionary.
#   Each node has a list of neighbours along with the edge cost.
#   Example: 'A':[('B',6),('F',3)] means:
#             From A → B (cost 6) and A → F (cost 3)

# h = {...}
# → This dictionary stores heuristic (estimated) values for each node.
#   These values represent how close each node is to the goal.

# ------------------------------------------------------
# FUNCTION: a_star(start, goal)
# ------------------------------------------------------
# pq = [(h[start], 0, [start])]
# → Initializes a priority queue with a tuple containing:
#    (f value, g value, path)
#    Initially, g = 0, and f = h[start]

# while pq:
#     f, g, path = heapq.heappop(pq)
# → Extracts the node with the smallest 'f' value (best estimated path).

# node = path[-1]
# → The last node in the path is the current node being explored.

# if node == goal: return path, g
# → If the goal node is reached, return the final path and total cost.

# for n, c in graph[node]:
#     heapq.heappush(pq, (g+c+h[n], g+c, path+[n]))
# → For each neighbour (n) of the current node:
#     - Calculate new g = current g + edge cost (c)
#     - Calculate new f = g + h[n]
#     - Add the new path to the priority queue

# return [], float('inf')
# → If no path is found, return an empty path and infinite cost.

# ------------------------------------------------------
# USER INPUT SECTION
# ------------------------------------------------------
# s = input("Start node: ")
# g = input("Goal node: ")
# → Takes start and goal nodes from the user.

# p, c = a_star(s, g)
# → Calls the A* function and gets the resulting path and total cost.

# print("Path:", ' → '.join(p))
# print("Cost:", c)
# → Prints the final shortest path and its total cost.

# ------------------------------------------------------
# 🧮 SAMPLE INPUT AND OUTPUT
# ------------------------------------------------------



# Explanation:
# Among all possible routes from A to J, 
# A* finds the path with the minimum total cost = 10.

# ------------------------------------------------------
# 🧠 SIMPLE UNDERSTANDING:
# ------------------------------------------------------
# A* finds the shortest path by combining:
#  - g(n): actual cost to reach a node
#  - h(n): estimated cost from that node to the goal
# It always selects the node with the lowest f(n) = g(n) + h(n)

# ------------------------------------------------------
# 🌍 REAL-TIME USES:
# ------------------------------------------------------
# 1. Google Maps and GPS navigation (finding shortest driving route)
# 2. Robotics (path planning for robots)
# 3. AI in games (NPCs finding optimal movement paths)
# 4. Network routing (optimizing data packet paths)
# ------------------------------------------------------

# 🕒 TIME COMPLEXITY:
#   In the worst case: O(E * log V)
#   (because of the priority queue operations)

# 💾 SPACE COMPLEXITY:
#

