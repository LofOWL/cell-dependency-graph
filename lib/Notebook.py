import json as js
from Cell import Cell
from AST import ASTProvider

bug_elements = ['!','%']

class Notebook:

	def __init__(self,nb_path):
		nb_sources = js.load(open(nb_path))
		self.cells = nb_sources['cells']
		self.cells_sources = [cell['source'] if type(cell['source']) == list else cell['source'].split("\n") for cell in self.cells if cell['cell_type'] == 'code']

	def get_producer_consumer(self):
		cell_map = list()
		index = 1
		ast = ASTProvider() 
		for cell_lines in self.cells_sources:
			ast.build('\n'.join([c for c in cell_lines if c and c[0] not in bug_elements]))
			c = Cell()
			c.set_producers_consumers(ast.producers,ast.consumers)
			c.set_index(index)
			cell_map.append(c)	
			index += 1
			ast.reset()
		return cell_map

	
if __name__ == "__main__":
	nb_path = '/Users/root1/Desktop/cell-dependency-graph/example/test.ipynb'
	nb = Notebook(nb_path)
	cm = nb.get_producer_consumer()
	print(cm)
        