import os
import sys
sys.path.insert(0,'./lib/')
from Notebook import Notebook
from Cell import Cell
from Utils import show_producer_consumer,clean_producer_consumer,generate_cdg,collect_before_producers
from CDGAnalyzer import CDGAnalyzer

notebook_path = lambda x: f'/media/lofowl/My Passport/CISC834/notebook_cache/{x}'

with open("/home/lofowl/Desktop/CISC843/project/data/data/final_len_3_notebooks.csv","r") as file:
    file = file.read().split("\n")[:-1]
    file = [i.split(",") for i in file]
    notebook_names = [i[0] for i in file]
    
def percentage_dependent_cells(cdg,cell_map):
    ca = CDGAnalyzer(cdg,cell_map)
    result = ca.get_cell_dependent()
    depedent_cells = [[i,j] for i,j in result.items() if len(j) >= 1]
    return len(depedent_cells) / len(result.keys())

def main():
    count = 0
    for notebook_name in notebook_names:
        try:
            nb_path = notebook_path(notebook_name)
            print(nb_path)
            nb = Notebook(nb_path)
            cell_map = nb.get_producer_consumer()
    
            # filter map
            clean_cell_map = clean_producer_consumer(cell_map)
            show_producer_consumer(clean_cell_map)

            # generator cell before


            cells_index = list(clean_cell_map.keys())

            cdg = generate_cdg(clean_cell_map)
            per_d = percentage_dependent_cells(cdg,clean_cell_map)
            print(per_d)
            count += 1
        except:
            pass
    print(count)

if __name__ == "__main__":
            #nb_path = '/media/lofowl/My Passport/CISC834/notebook_cache/c2bedd3921fecd401ebf1c7b126d85a92fa2e17a_pandas-munging#pandas_data_munging.ipynb'
            nb_path = './example/titanic.ipynb'
            nb = Notebook(nb_path)
            cell_map = nb.get_producer_consumer()
            # convert to cell class
            cell_map = [Cell(item) for item in cell_map.items()]

            #filter map
            clean_cell_map = clean_producer_consumer(cell_map)
            show_producer_consumer(clean_cell_map)

            # generate before cell
            filter_cell_map = collect_before_producers(clean_cell_map)
            show_producer_consumer(filter_cell_map)

            # generate cdg
            cdg = generate_cdg(filter_cell_map)
            cdg.show(cdg.root,'   ')
            per_d = percentage_dependent_cells(cdg,filter_cell_map)
            print(per_d)