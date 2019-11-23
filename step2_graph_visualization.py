
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
    graph.to_png("graph")
 