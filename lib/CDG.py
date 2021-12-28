from copy import deepcopy
from collections import Counter

class GroupNode:

    def __init__(self,*nodes):
        self.Nodes = list(nodes)
        self.children = list()

    # condition to group
    def is_group(self,node):
        compare = self.Nodes[-1]
        #return compare.consumers == node.consumers and compare.producers != node.producers
        return Counter(compare.other_consumers) == Counter(node.other_consumers) or node.other_consumers == []

    def add(self,node):
            self.Nodes += [node]

    def generate(self):
        self.cells = [cell.cell for cell in self.Nodes]
        self.producers = [producer for node in self.Nodes for producer in node.producers]
        self.consumers = [producer for node in self.Nodes for producer in node.consumers]
        self.other_consumers = [consumer for consumer in self.consumers if consumer not in self.producers]


    def __str__(self):
        return ','.join([str(cell.cell) for cell in self.Nodes])

class Node:

    def __init__(self,cell):    
        self.cell = cell.index
        self.producers = cell.producers
        self.consumers = cell.consumers
        self.before_producers = cell.before_producers
        self.other_consumers = cell.other_consumers
        self.children = list()

    def __str__(self):
        return f'{self.cell}'

class CDG:

    def __init__(self):
        self.root = None

    def insert(self,node,producers,cells,cell_map):
        if cells:
            children = list()
            # find all the children
            for cell in cells:
                if all(consumer in producers for consumer in cell.other_consumers):
                    children.append(deepcopy(cell))

            # grouping the children
            group_children = list()
            for i in range(len(children)):
                if i == 0:
                    group_children.append(GroupNode(children[i]))
                else:
                    group_children[0].add(children[i])
            #for child in children:
            #    isGroup = False
            #    for gc in group_children:
            #        if gc.is_group(child):
            #            gc.add(child)
            #            isGroup = True
            #            break
            #    if not isGroup: group_children.append(GroupNode(child)) 

            for i in group_children: 
                i.generate()

            node.children = group_children
            for child in node.children:
                self.insert(child,producers + child.producers,[cell for cell in cells if cell.cell not in child.cells],cell_map)

    def show(self,start,space):
        print(f'{space}{start}')
        for child in start.children:
            self.show(child,' '*len(space)+' '*4)

    def find(self,start,target,alist):
        if isinstance(start,Node):
            if start.cell == target: 
                alist.append(start)
                return 
        else:
            if target in start.cells:
                alist.append(start)
                return
        for child in start.children:
                self.find(child,target,alist) 

    def list_all_cells(self,start,alist):
        alist += [c.cell for c in start.children if isinstance(c,Node)]
        alist += [i for c in start.children for i in c.cells if isinstance(c,GroupNode)]
        for child in start.children:
            self.list_all_cells(child,alist)

    def all_nodes(self,start,nodes=list()):
        nodes.append(start)
        for child in start.children:
            nodes += self.all_nodes(child)
        return nodes


if __name__ == "__main__":
    fake = {1:[['random','Image','a'],['a']],2:[['b'],['a','b']],3:[[],['b']],4:[[],['a','b']],5:[[],[]]}
    nodes = [Node(cell) for cell in list(fake.items())]
    cdg = CDG()
    cdg.root = nodes.pop(0)
    cdg.insert(cdg.root,cdg.root.producers,nodes)
    cdg.show(cdg.root,'    ')