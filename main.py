from lib.notebook import Notebook
from lib.AST import ASTProvider
from lib.CDG import CDG,Node



if __name__ == "__main__":
    nb_path = "./example/test.ipynb"
    nb = Notebook(nb_path)
    astp = ASTProvider()
    cell_map = dict()
    index = 1
    for cell in nb.cells_sources:
        astp.build(''.join(cell))
        cell_map[index] = [astp.producers,astp.consumers]
        astp.reset()

        index += 1
    
    for value,item in cell_map.items():
        print(f'{value} {item}')
    

    nodes = [Node(cell) for cell in list(cell_map.items())]
    cdg = CDG()
    cdg.root = nodes.pop(0)
    cdg.insert(cdg.root,cdg.root.producers,nodes)
    cdg.show(cdg.root,' ')
    