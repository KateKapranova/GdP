#cycle detection on undirected graphs
#DFS algorithm

#V=[0,1,2]
#E=[[1],[0,2],[1]]  #cyclefree edges
#E=[[1,2],[0,2],[0,1]] #edges with a cycle

#V=[0,1,2,3,4]
#E=[[1,2,3],[0],[0,4],[0],[2]]#no cycle
#E=[[1,2,3],[0],[0,4],[0,4],[2,3]]#cycle

V=[0,1,2,3,4,5]
#E=[[1,2,3],[0],[0,4],[0],[2,5],[4]]#no cycle
E=[[1,2,3],[0],[0,4],[0,5],[2,5],[4,3]]#cycle

def cycleDFS(V,E):
    visited=[0]*len(V)
    previous=[-1]*len(V)
    stack=[]
    result='cycle not detected'
    for v in range(len(V)):
        print('iteration ', v)
        if v not in stack and visited[v]==0:
            stack.append(v)
            print('stack= ', stack)
        while (len(stack)>0):
            current=stack[len(stack)-1]
            print('current =', current)
            visited[current]=1
            neighbours = len(E[current])
            if neighbours>0:
                for i in range(0,len(E[current])):
                    print("inside i", i)
                    if visited[E[current][i]]==0:
                        visited[E[current][i]]=1
                        stack.append(E[current][i])
                        print('inside stack= ', stack)
                        previous[E[current][i]]=current
                        print('previous',previous)
                        print('break')
                        break
                    elif visited[E[current][i]]==1:
                        print('visited= ',visited)
                        if previous[current]==E[current][i]:
                            if i==(neighbours-1):
                                stack.pop()
                                print('pop')
                                print('break')
                                break
                            print('continue')
                            continue

                        elif previous[current]!=E[current][i] and previous[E[current][i]]!=current and previous[current]!=-1:
                            return 'Cycle detected'
                        else:
                            stack.pop()
            else:
                stack.pop() #we hardly ever get here
    return result

print(cycleDFS(V,E))
