

class Graph:
    def __init__(self):
        self.graph=dict()

    def add_node(self,node_name,color):
        self.graph[node_name]=[[],color]

    def add_edge(self,u,v):
        self.graph[u][0].append(v)

    def get_node_number(self):
        return len(self.graph)
    #print
    def __repr__(self):
        s=""
        for i in range(self.get_node_number()):
            line="node %d [color %d]: "%(i,self.graph[i][1])+" ".join([str(k) for k in self.graph[i][0]])+"\n"
            s+=line
        return s
    def __str__(self):
        return self.__repr__()

    def to_png(self,name="graph"):
        num_nodes=self.get_node_number()
        # graph_type: digraph (direct)
        # graph_name:
        # shape type: circle
        dot="digraph \"%s\" {\nnode [shape=circle];\n"%name
        # all nodes value, label
        cmap={0:"red",1:"yellow"}
        for i in range(num_nodes):
            dot+="node_%d [label=\"%d\",style=filled,color=%s];\n"%(i,i,cmap[self.graph[i][1]])
        # all edges
        for i in range(num_nodes):
            for j in self.graph[i][0]:
                dot+="node_%d -> {node_%d};\n"%(i,j)
        dot+="}"
        import pydot
        g=pydot.graph_from_dot_data(dot)[0]
        g.write_png(name+".png")
        print("[%s.png] saved !"%name)
        # g.write(name+".txt")

    

    def BFS(self,v,visited_list):
        # if no child, return
        if len(self.graph[v][0])==0:
            return visited_list

        # if has child, add its childs fisrt, then recursively run its childs
        v_child = self.graph[v][0]
        not_visisted_list = [k for k in v_child if k not in visited_list]
        visited_list+=not_visisted_list

        for k in not_visisted_list:
            self.BFS(k,visited_list)

        return visited_list

    def BFS1(self,v):
        visited=[False]*self.get_node_number()
        queue=[v]
        visited[v]=True
        outlist=[]
        while len(queue)>0:
            s = queue.pop(0)
            outlist.append(s)
            for k in self.graph[s][0]:
                if visited[k]==False:
                    queue.append(k)
                    visited[k]=True
        return outlist

    def DFS(self,v,visited_list):
        visited_list.append(v)
        # if no child, return
        if len(self.graph[v][0])==0:
            return visited_list
        # if has child, add its childs fisrt, then recursively run its childs
        v_child = self.graph[v][0]
        not_visisted_list = [k for k in v_child if k not in visited_list]
        for k in not_visisted_list:
            self.DFS(k,visited_list)
        return visited_list

    def topologic_sort(self,v,visited_list):
        # if no child, return
        if len(self.graph[v][0])==0:
            visited_list.insert(0,v)
            return visited_list

        # if has child, add its childs fisrt, then recursively run its childs
        v_child = self.graph[v][0]
        not_visisted_list = [k for k in v_child if k not in visited_list]
        for k in not_visisted_list:
            self.topologic_sort(k,visited_list)
        visited_list.insert(0,v)
        return visited_list

    #by definition
    def topologic_sort1(self):
        indegree={}
        num_nodes=self.get_node_number()
        for u in range(num_nodes):
            indegree[u]=0
        # indegree info
        for u in range(num_nodes):
            for v in self.graph[u][0]:
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
            for v in self.graph[u][0]:
                indegree[v]-=1
                if indegree[v]==0:
                    no_depend_list.append(v)
        return mylist

    def get_all_subs_path(self,v,dst,paths):
        if v==dst:
            return paths
        
        all_path=[]
        for u in self.graph[v][0]:
            paths_u = [k[:]+[u] for k in paths]
            all_path+=self.get_all_subs_path(u,dst,paths_u)
        return all_path


if __name__ =="__main__":
    graph=Graph()
    graph.add_node(0,0)
    graph.add_node(1,0)
    graph.add_node(2,1)
    graph.add_node(3,0)
    graph.add_node(4,1)
    graph.add_node(5,0)

    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(2,4)
    graph.add_edge(1,4)
    graph.add_edge(4,3)
    graph.add_edge(3,5)
    graph.add_edge(4,5)
    print(graph)
    graph.to_png("graph1")

    # # breadth_first_search
    # print("BFS: ",graph.BFS(0,[0]))
    # print("BFS1: ",graph.BFS1(0))
 
    # # depth_first_search
    # print("DFS: ",graph.DFS(0,[]))

    # #topologic sort
    # print("sort: ", graph.topologic_sort(0,[]))
    # print("sort1: ", graph.topologic_sort1())

    # print("all path from 0-5:\n",graph.get_all_subs_path(0,5,[[0]]))