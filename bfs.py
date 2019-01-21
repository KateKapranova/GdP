#BFS implemented with adjacency lists represented as lists in a list
#problem statement: a function is called with a list of airports,
#adjacency lists for each airport and a start airport
#return a list of airports which can be reached from the starting airport

V = ['CGN','FRA','KEL','MUC','PAD','SXF','STR','TGL']
# airports are referred to by their index in the list
E = [[1,4],[0,3,6],[6],[2],[2],[7],[1],[5]]
start = 'KEL'

#we assume start is a string
def BFS(start, V,E):
    #initialise the needed lists for queue, result and visited nodes
    queue = []
    result = []
    visited = [0] * len(V) #initially none of the nodes is visited
    #look for the index of the start node and mark it as visited
    for index in range(len(V)):
        if start == V[index]:
            visited[index]=1
            queue.append(index)
    #start the BFS and execute the loop instructions until queue is empty
    while len(queue) > 0:
        #queue implementation: the factually last element in the list will
        #be considered the first element of the queue
        #the new elements will be inserted at the beginning of the list

        #start with the first element in the queue
        current = queue.pop()
        #we execute the search only if a node has children
        if len(E[current])>0:
            for i in range(len(E[current])):
                #search for unvisited neighbours
                if visited[E[current][i]] == 0:
                    queue.insert(0,E[current][i])
                    visited[E[current][i]]=1
                    #here we define the sequence in which the elements are added
                    #to the result list. principle applied here: found-> added
                    result.append(E[current][i])
    #a help loop to return list of airports by name, not by index
    for k in range(len(result)):
        index = result[k]
        result[k]=V[index]
    return result

print(BFS(start,V,E))
