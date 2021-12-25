from CDG import CDG,Node

def clean_producer_consumer(cell_map):
    return {i:j for i,j in cell_map.items() if j[0] and j[1]}

def show_producer_consumer(cell_map):
    for i,j in cell_map.items():
        print(f"{i} \nP:{j[0]} \nC:{j[1]}") 

def generate_cdg(cell_map):
    nodes = [Node(cell) for cell in list(cell_map.items())]
    cdg = CDG()
    cdg.root = nodes.pop(0)
    cdg.insert(cdg.root,cdg.root.producers,nodes)
    cdg.show(cdg.root,'   ')

if __name__ == "__main__":
    print("Utils")
