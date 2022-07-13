import os
import sys
sys.path.insert(0,'./lib/')
from Notebook import Notebook
from Utils import *
from SnippetCode import SnippetCode

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


    cdg = generate_cdg(clean_cell_map)
    cdg.show(cdg.root,'   ')

    sc = SnippetCode(clean_cell_map)
    psnippet,prsnippet = sc.rankSnippet(sc.getSnippet(12))
    print(psnippet)