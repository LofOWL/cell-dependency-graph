import json as js
from AST import ASTProvider
from Cell import Cell

bug_elements = ['!','%']

class Notebook:

	def __init__(self,nb_path):
		nb_sources = js.load(open(nb_path))
		self.cells = nb_sources['cells']
		self.cells_sources = [cell['source'] if type(cell['source']) == list else cell['source'].split("\n") for cell in self.cells if cell['cell_type'] == 'code']

	def get_producer_consumer(self):
		astp = ASTProvider()
		#cell_map = dict()
		cell_map = list()
		index = 1
		for cell in self.cells_sources:
			astp.build('\n'.join([c for c in cell if c and c[0] not in bug_elements]))
			#cell_map[index] = [astp.producers,astp.consumers]
			cell_map.append(Cell([index,[astp.producers,astp.consumers]]))
			astp.reset()

			index += 1
		return cell_map

	
if __name__ == "__main__":
	nb_path = 'sartorius-mask-rcnn-efficientnetv2-train-2h.ipynb'
	nb = Notebook(nb_path)
	
        