from CDG import CDG,Node

def clean_producer_consumer(cell_map):
    return {i:j for i,j in cell_map.items() if j[0] and j[1]}

def show_producer_consumer(cell_map):
    for i,j in cell_map.items():
        print(f"{i} \nP:{j[0]} \nC:{j[1]} \nCC:{j[2]}") 

def collect_before_producers(cell_map,index):
    producers = list()
    for cell,values in cell_map.items():
        if index != cell:
            producers += values[0]
        else:
            break
    return producers

def generate_cdg(cell_map):
    nodes = [Node(cell) for cell in list(cell_map.items())]
    cdg = CDG()
    cdg.root = nodes.pop(0)
    cdg.insert(cdg.root,cdg.root.producers,nodes,cell_map,collect_before_producers)
    # cdg.show(cdg.root,'   ')
    return cdg 

def find_cell_behind(cdg,target):
    find_2 = list()
    cdg.find(cdg.root,target,find_2)

    unique = list()    
    for node in find_2:
        node_list = list()
        cdg.list_all_cells(node,node_list)
        unique += node_list
        
    return list(set(unique))

if __name__ == "__main__":
    print("Utils")
