from CDG import CDG,Node

def clean_producer_consumer(cell_map):
    return [cell for cell in cell_map if cell.producers or cell.consumers]

def show_producer_consumer(cell_map):
    for cell in cell_map: print(cell)

def collect_before_producers(cell_map):
    for ccell in cell_map:
        producers = list()
        for cell in cell_map:
            if ccell.index > cell.index:
                producers += cell.producers
        ccell.set_before_producers(producers)
    return cell_map

def generate_cdg(cell_map):
    nodes = [Node(cell) for cell in cell_map]
    cdg = CDG()
    cdg.root = nodes.pop(0)
    cdg.insert(cdg.root,cdg.root.producers,nodes,cell_map)
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
