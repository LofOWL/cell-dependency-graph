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

    def insert(self,node,producers,cells,cell_map,collect_before_producers):
        if cells:
            children = list()
            for cell in cells:
                before_p = collect_before_producers(cell_map,cell.cell) 
                current_producers = [producer for producer in cell.producers if producer not in before_p]
                if all(consumer in (producers + current_producers) for consumer in cell.consumers):
                    children.append(deepcopy(cell))
            node.children = children
            for child in children:
                self.insert(child,producers + child.producers,[cell for cell in cells if cell.cell != child.cell],cell_map,collect_before_producers)

    def show(self,start,space):
        if start.children:
            print(f'{space}{start}')
            for child in start.children:
                self.show(child,' '*len(space)+' '*4)

    def find(self,start,target,alist):
        if start.children:
            if start.cell == target: 
                alist.append(start)
                return 
            for child in start.children:
                self.find(child,target,alist) 

    def list_all_cells(self,start,alist):
        if start.children:
            alist += [c.cell for c in start.children]
            for child in start.children:
                self.list_all_cells(child,alist)


if __name__ == "__main__":
    fake = {1:[['random','Image','a'],['a']],2:[['b'],['a','b']],3:[[],['b']],4:[[],['a','b']],5:[[],[]]}
    nodes = [Node(cell) for cell in list(fake.items())]
    cdg = CDG()
    cdg.root = nodes.pop(0)
    cdg.insert(cdg.root,cdg.root.producers,nodes)
    cdg.show(cdg.root,'    ')