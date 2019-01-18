#DFS implemented with adjacency lists represented as lists in a list
#problem statement: a function is called with a list of airports V,
#adjacency lists for each airport E and a start airport
#return a list of airports which can be reached from the starting airport

V = ['CGN','FRA','KEL','MUC','PAD','SXF','STR','TGL']
# airports are referred to by their index in the list
E = [[1,4],[0,3,6],[6],[2],[2],[7],[1],[5]]
start = 'FRA'

#we assume start is a string
def DFS(start, V,E):
    #initialise the needed lists for stack, result and visited nodes
    stack = []
    result = []
    visited = [0] * len(V) #initially none of the nodes is visited
    #look for the index of the start node and mark it as visited
    for index in range(len(V)):
        if start == V[index]:
            visited[index]=1
            stack.append(index)
    #start the DFS and execute the loop instructions until stack is empty
    while len(stack) > 0:
        #look at the upper node on the stack
        current = stack[len(stack)-1]
        #number of neigbours of the current node
        neigbours = len(E[current])
        #we execute the search only if a node has children
        if neigbours>0:
            for i in range(len(E[current])):
                #search for unvisited neighbours
                if visited[E[current][i]] == 0:
                    stack.append(E[current][i])
                    #print('append stack with: ', E[current][i])
                    visited[E[current][i]]=1
                    result.append(E[current][i])
                    #print('append result list with: ', E[current][i])
                    break
                #if we visited all the neigbours, current is removed from stack
                elif i==(neigbours-1) and visited[E[current][i]] == 1:
                    garbage = stack.pop()
                    #print('remove from stack:', garbage)
        #if a node doesn't have neigbours, pop it out
        else:
            stack.pop()
    #a help loop to return list of airports by name, not by index
    for k in range(len(result)):
        index = result[k]
        result[k]=V[index]

    return result

print(DFS(start,V,E))
