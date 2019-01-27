#algorithm determines if a graph is bipartite
#input: graph G
#output: true if G is bipartite, else false

V = ['CGN','FRA','KEL','MUC','PAD','SXF','STR','TGL']
# airports are referred to by their index in the list
E = [[1,4],[0,3,6],[6],[2],[2],[7],[1],[5]]
start = 'KEL'

#we assume start is a string
def BFS(start, V,E):
    #initialise the needed lists for queue, result and visited nodes
    result = 'true'
    queue = []
    bip_check = []
    visited = [0] * len(V) #initially none of the nodes is visited
    bip_check = [2]*len(V) #initially nodes are not assigned to subsets

    #repeat as long as there are unchecked nodes (value 2 means unchecked)
    while ((2 in bip_check) == True):
        for index in range(len(V)):
            if start == V[index]:
                bip_check[index]=0
                queue.append(index)

        #start the BFS and execute the loop instructions until queue is empty
        while len(queue) > 0:
            #queue implementation: the factually last element in the list will
            #be considered the first element of the queue
            #the new elements will be inserted at the beginning of the list

            #start with the first element in the queue
            #we execute the search only if a node has children
            current = queue.pop()
            if len(E[current])>0:
                for i in range(len(E[current])):
                    #search for unvisited neighbours
                    if bip_check[E[current][i]] == 2:
                        queue.insert(0,E[current][i])
                        bip_check[E[current][i]]=1-bip_check[current]
                        #here we define the sequence in which the elements are added
                        #to the result list. principle applied here: found-> added
                    elif bip_check[E[current][i]] == bip_check[current]:
                        return 'false'
    return result

print(BFS(start,V,E))
