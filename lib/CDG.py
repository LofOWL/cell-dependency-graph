from copy import deepcopy

class Node:

    def __init__(self,cell):    
        self.cell = cell[0]
        self.producers = cell[1][0]
        self.consumers = cell[1][1]
        self.other_consumers = [consumer for consumer in self.consumers if consumer not in self.producers]
        self.children = list()

    def __str__(self):
        return f'{self.cell}'

class CDG:

    def __init__(self):
        self.root = None

    def insert(self,node,producers,cells):
        if cells:
            children = list()
            for cell in cells:
                if all(consumer in producers for consumer in cell.other_consumers):
                    children.append(deepcopy(cell))
            node.children = children
            for child in children:
                self.insert(child,producers + child.producers,[cell for cell in cells if cell.cell != child.cell])

    def show(self,start,space):
        if start.children:
            print(f'{space}{start}')
            for child in start.children:
                self.show(child,space*2)

if __name__ == "__main__":
    fake = {1:[['random','Image','a'],['a']],2:[['b'],['a','b']],3:[[],['b']],4:[[],['a','b']],5:[[],[]]}
    nodes = [Node(cell) for cell in list(fake.items())]
    cdg = CDG()
    cdg.root = nodes.pop(0)
    cdg.insert(cdg.root,cdg.root.producers,nodes)
    cdg.show(cdg.root,' ')