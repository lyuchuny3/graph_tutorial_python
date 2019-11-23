class Graph:
    def __init__(self,num_nodes):
        self.num_nodes=num_nodes
        self.graph=[[] for i in range(num_nodes)]

    def add_edge(self,u,v):
        self.graph[u].append(v)


    #print
    def __repr__(self):
        s=""
        for i in range(self.num_nodes):
            line="node %d: "%i+" ".join([str(k) for k in self.graph[i]])+"\n"
            s+=line
        return s
    def __str__(self):
        return self.__repr__()

    def to_png(self,name="graph"):
        # graph_type: digraph (direct)
        # graph_name:
        # shape type: circle
        dot="digraph \"%s\" {\nnode [shape=circle];\n"%name
        # all nodes value, label
        for i in range(self.num_nodes):
            dot+="node_%d [label=\"%d\"];\n"%(i,i)
        # all edges
        for i,v in enumerate(self.graph):
            for j in v:
                dot+="node_%d -> {node_%d};\n"%(i,j)
        dot+="}"
        import pydot
        g=pydot.graph_from_dot_data(dot)[0]
        g.write_png(name+".png")
        print("[%s.png] saved !"%name)
        # g.write(name+".txt")
    

    def BFS(self,v,visited_list):
        # if no child, return
        if len(self.graph[v])==0:
            return visited_list

        # if has child, add its childs fisrt, then recursively run its childs
        v_child = self.graph[v]
        not_visisted_list = [k for k in v_child if k not in visited_list]
        visited_list+=not_visisted_list

        for k in not_visisted_list:
            self.BFS(k,visited_list)

        return visited_list

    def BFS1(self,v):
        visited=[False]*self.num_nodes
        queue=[v]
        visited[v]=True
        outlist=[]
        while len(queue)>0:
            s = queue.pop(0)
            outlist.append(s)
            for k in self.graph[s]:
                if visited[k]==False:
                    queue.append(k)
                    visited[k]=True
        return outlist

    def DFS(self,v,visited_list):
        visited_list.append(v)
        # if no child, return
        if len(self.graph[v])==0:
            return visited_list
        # if has child, add its childs fisrt, then recursively run its childs
        v_child = self.graph[v]
        not_visisted_list = [k for k in v_child if k not in visited_list]
        for k in not_visisted_list:
            self.DFS(k,visited_list)
        return visited_list

    def topologic_sort(self,v,visited_list):
        # if no child, return
        if len(self.graph[v])==0:
            visited_list.insert(0,v)
            return visited_list

        # if has child, add its childs fisrt, then recursively run its childs
        v_child = self.graph[v]
        not_visisted_list = [k for k in v_child if k not in visited_list]
        for k in not_visisted_list:
            self.topologic_sort(k,visited_list)
        visited_list.insert(0,v)
        return visited_list

    #by definition
    def topologic_sort1(self):
        indegree={}
        for u in range(self.num_nodes):
            indegree[u]=0
        # indegree info
        for u in range(self.num_nodes):
            for v in self.graph[u]:
                indegree[v]+=1
        # no depend list (indegree==0)
        no_depend_list=[]
        for u in indegree:
            if indegree[u]==0:
                no_depend_list.append(u)
        mylist=[]
        while len(no_depend_list)>0:
            u = no_depend_list.pop(0)
            mylist.append(u)
            # remove edges
            for v in self.graph[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    no_depend_list.append(v)
        return mylist

    # def topological_sort(self,path,stack):
    #     #print("path=",path,"stack=",stack)
    #     if len(path)==0:
    #         return stack[::-1]
        
    #     s = path[-1] #last one
    #     not_visit_child = [n for n in self.graph[s] if n not in stack]
    #     if len(not_visit_child)==0:
    #         path.pop()
    #         stack.append(s)
    #         self.topological_sort(path,stack)
    #     else:
    #         path.append(not_visit_child[0])
    #         self.topological_sort(path,stack)
    #     return stack[::-1]

if __name__ =="__main__":
    graph=Graph(6)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(2,4)
    graph.add_edge(1,4)
    graph.add_edge(4,3)
    graph.add_edge(3,5)
    graph.add_edge(4,5)
    print(graph)
    # graph.to_png("graph")

    # # breadth_first_search
    # print("BFS: ",graph.BFS(0,[0]))
    # print("BFS1: ",graph.BFS1(0))
 
    # # depth_first_search
    # print("DFS: ",graph.DFS(0,[]))

    #topologic sort
    print("sort: ", graph.topologic_sort(0,[]))
    print("sort1: ", graph.topologic_sort1())