from os.path import exists

class Graph:
    def __init__(self):
        self.edges = []
        self.file = None
    
    def read_file(self, filename):
        if exists(filename):
            self.file = filename
            f = open(self.file, 'r')
            data = f.read().split()
            for each in data:
                tup = (int(each[1]), int(each[3]))
                self.edges.append(tup)
                
            f.close()
        else:
            print("File doesnt exist")

    def add_edge(self, edge):
        if edge in self.edges:
            print("Edge already exists")
        else:
            f = open(self.file, 'a')
            f.write(f" {edge}")
            f.close()
            print("Edge added to file")

    def remove_edge(self, edge):
        if edge not in self.edges:
            print("Edge not in file")
        else:
            self.edges = [(x,y) for (x,y) in self.edges if (x,y) != edge]
            f = open(self.file, 'w')
            for each in self.edges:
                f.write(f"({each[0]},{each[1]}) ")
            f.close()
            print("Edge removed from file")

    def display_nodes_edges(self):
        
        nodes = set([x for (x,y) in self.edges] + [y for (x,y) in self.edges])
        print(f"Nodes are: {nodes}")
        print(f"edges are : {self.edges}")

    def neighbours(self, node):
        if node not in set([x for (x,y) in self.edges] + [y for (x,y) in self.edges]):
            print("Invalid node")
        else:
            neighbours = []
            for each in self.edges:
                if node in each:
                    neightbour = each[0] if each[1] == node else each[1]
                    neighbours.append(neightbour)
            print(f"Neightbours of {node} are {neighbours}")

o = Graph()
o.read_file('1.txt')
# o.add_edge((1,5))
# o.remove_edge((2,3))
o.display_nodes_edges()
o.neighbours(3)
