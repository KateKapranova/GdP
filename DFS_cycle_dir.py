#DFS Cycle detection on directed graphs
#aka detecting a back edge

#V=[0,1,2,3,4,5]
#E=[[1,2],[3],[4],[],[5],[2]]#directed graph with a cycle

V=[0,1,2,3,4]
E=[[1,3],[2],[],[4],[]] #directed graph without a cycle

def cycleDetect(V,E):
    visited = [0]*len(V)
    stack=[]
    for v in range(len(V)):
        stack.append(v)
        visited[v]=1
        while (len(stack)>0):
            current = stack[len(stack)-1]
            if len(E[current])>0:
                for i in range(0,len(E[current])):
                    if visited[E[current][i]]==0:
                        visited[E[current][i]]=1
                        stack.append(E[current][i])
                        break
                    elif visited[E[current][i]]==1 and ((E[current][i] in stack) == True):
                            return 'cycle detected'
                    else:
                        stack.pop()
            else:
                stack.pop()
    return 'cycle not detected'

print(cycleDetect(V,E))
