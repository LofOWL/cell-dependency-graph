import json as js

class Notebook:

	def __init__(self,nb_path):
		nb_sources = js.load(open(nb_path))
		self.cells = nb_sources['cells']
		self.cells_sources = [cell['source'] for cell in self.cells if cell['cell_type'] == 'code']

if __name__ == "__main__":
	nb_path = 'sartorius-mask-rcnn-efficientnetv2-train-2h.ipynb'
	nb = Notebook(nb_path)
	
        