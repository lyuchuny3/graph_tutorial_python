
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
 