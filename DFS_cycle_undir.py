#cycle detection on undirected graphs
#DFS algorithm

#V=[0,1,2]
#E=[[1],[0,2],[1]]  #cyclefree edges
#E=[[1,2],[0,2],[0,1]] #edges with a cycle

#V=[0,1,2,3,4]
#E=[[1,2,3],[0],[0,4],[0],[2]]#no cycle
#E=[[1,2,3],[0],[0,4],[0,4],[2,3]]#cycle

#V=[0,1,2,3,4,5]
#E=[[1,2,3],[0],[0,4],[0],[2,5],[4]]#no cycle
#E=[[1,2,3],[0],[0,4],[0,5],[2,5],[4,3]]#cycle

def cycleDFS(V,E):
    visited=[0]*len(V)
    previous=[-1]*len(V)
    stack=[]
    result='Cycle not detected'
    for v in range(len(V)):
        if v not in stack and visited[v]==0:
            stack.append(v)
        while (len(stack)>0):
            current=stack[len(stack)-1]
            visited[current]=1
            neighbours = len(E[current])
            if neighbours>0:
                for i in range(0,len(E[current])):
                    if visited[E[current][i]]==0:
                        visited[E[current][i]]=1
                        stack.append(E[current][i])
                        previous[E[current][i]]=current
                        break
                    elif visited[E[current][i]]==1:
                        if previous[current]==E[current][i]:
                            if i==(neighbours-1):
                                stack.pop()
                                break
                            continue
                        elif previous[current]!=E[current][i] and previous[E[current][i]]!=current and previous[current]!=-1:
                            return 'Cycle detected'
                        else:
                            stack.pop()
            else:
                stack.pop() #we get here in case of a detached node
    return result

print(cycleDFS(V,E))
