from queue import PriorityQueue

# best first algorithm
def best_first_search(source, target, n):
    visited = [False for _ in range(n)]
    # keep track of visited nodes
    visited[0] = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying path which has lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()

# Function for adding edges to graph

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
N = int(input("Number of nodes: "))
E = int(input("Number of edges: "))

graph = [[] for _ in range(N)]

for _ in range(E):
    x,y,cost=input("Enter edge: ").split(",")
    addedge(int(x),int(y),int(cost))

source = int(input("Enter the source: "))
target = int(input("Enter the target: "))

print("\nBest first search: \n")
best_first_search(source, target, N)
