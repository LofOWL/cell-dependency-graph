import os
import sys
sys.path.insert(0,'./lib/')
from notebook import Notebook
from Utils import show_producer_consumer,clean_producer_consumer,generate_cdg,find_cell_behind

if __name__ == "__main__":
    nb_path = "./example/titanic.ipynb"
    nb = Notebook(nb_path)
    cell_map = nb.get_producer_consumer()

    # filter map
    clean_cell_map = clean_producer_consumer(cell_map)
    #show_producer_consumer(clean_cell_map)
    cells_index = list(clean_cell_map.keys())
    print(cells_index)

    cdg = generate_cdg(clean_cell_map)

    cell_below = {i:[] for i in cells_index}
    for index,alist in cell_below.items():
        alist += find_cell_behind(cdg,index)
    
    for i,j in cell_below.items(): print(f'{i} {j}\n')