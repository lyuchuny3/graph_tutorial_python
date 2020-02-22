

class Graph:
    def __init__(self):
        self.graph=dict()

    def add_node(self,node_name):
        self.graph[node_name]=[]

    def add_edge(self,u,v,weight):
        self.graph[u].append([v,weight])

    def get_node_number(self):
        return len(self.graph)
    #print
    def __repr__(self):
        s=""
        for i in range(self.get_node_number()):
            line="node %d: "%(i)+" ".join(["("+str(v)+","+str(w)+")" for v,w in self.graph[i]])+"\n"
            s+=line
        return s
    def __str__(self):
        return self.__repr__()

    def to_png(self,name="graph"):
        '''
        http://www.webgraphviz.com/
        see graph4.txt for detail
        # rankdir=LR  (left->right)
        # rankdir=BT  (bottom->top)
        '''
        num_nodes=self.get_node_number()
        dot="digraph \"%s\" {\nrankdir=LR;\nnode [shape=circle];\n"%name
        # all nodes
        dot+="node_%d [label=\"%d\",style=filled,color=green];\n"%(0,0)
        for i in range(1,num_nodes-1):
            dot+="node_%d [label=\"%d\",style=filled,color=yellow];\n"%(i,i)
        dot+="node_%d [label=\"%d\",style=filled,color=red];\n"%(num_nodes-1,num_nodes-1)
        # all edges
        for u in range(num_nodes):
            for v,weight in self.graph[u]:
                dot+="node_%d -> node_%d [label=\"%d\"];\n"%(u,v,weight)
        dot+="}"
        import pydot
        g=pydot.graph_from_dot_data(dot)[0]
        g.write_png(name+".png")
        print("[%s.png] saved !"%name)
        g.write(name+".txt")

    def get_small_vertex(self,mydir,unvisited):
        dist=float('inf')
        idx = -1
        for i in unvisited:
            if mydir[i][0]<dist:
                idx=i
                dist=mydir[i][0]
        return idx
    def dijkstra(self,start=0,end=0):
        n=self.get_node_number()
        # init dict =======================
        dist=dict()
        for i in range(n):
            if(i==start):
                dist[i]=(0,-1)
            else:
                dist[i]=(float('inf'),-1)
        
        visited=[]
        unvisited=[i for i in  range(n)]
        while(len(unvisited)>0):
            #pop smallest u,  visited, unvisited =======
            u=self.get_small_vertex(dist,unvisited)
            visited.append(u)
            unvisited.remove(u)

            # for v in u.neigbour, update distant===========
            for v,weight in self.graph[u]:
                new_dist=dist[u][0]+weight
                if new_dist<dist[v][0]:
                    dist[v]=(new_dist,u)
        print(dist)
        ret=[end]
        v=end
        while(start not in ret):
            ret.append(dist[v][1])
            v=ret[-1]
        print("->".join(str(i) for i in ret[::-1]))

def load_graph_from_cfg(cfgfile=None):
    number_of_nodes=0
    mode=None
    graph=Graph()
    with open(cfgfile,"r") as f:
        lines=[k.strip() for k in f if k.strip()!=""]
        for line in lines:
            if line.startswith("N"):
                mode="Node"
                number_of_nodes=int(line.split()[-1])
                for i in range(number_of_nodes):
                    graph.add_node(i)
                continue
            if line.startswith("E"):
                mode="Edge"
                continue
            if mode=="Edge":
                u,v,weight=line.split(" ")
                graph.add_edge(int(u),int(v),int(weight))
    return graph

if __name__ =="__main__":
    # graph4/graph5 cfg
    graph = load_graph_from_cfg("graph4.cfg")
    print(graph)
    graph.to_png("graph4")
    graph.dijkstra(0,graph.get_node_number()-1)
