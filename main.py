import os
import sys
sys.path.insert(0,'./lib/')
from notebook import Notebook
from Utils import show_producer_consumer,clean_producer_consumer,generate_cdg
from CDG import CDG,Node
from tqdm import tqdm

bug_elements = ['!','%']

if __name__ == "__main__":
    nb_path = "./example/titanic.ipynb"
    nb = Notebook(nb_path)
    cell_map = nb.get_producer_consumer()

    # show map
    show_producer_consumer(cell_map)

    # filter map
    clean_cell_map = clean_producer_consumer(cell_map)
    show_producer_consumer(clean_cell_map)

    generate_cdg(clean_cell_map)