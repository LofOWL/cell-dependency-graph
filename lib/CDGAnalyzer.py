from Utils import find_cell_behind


class CDGAnalyzer:

    def __init__(self,cdg,cell_map):
        self.cdg = cdg
        self.cell_map = cell_map

    def get_cell_dependent(self):
        cells_index = [cell.index for cell in self.cell_map]
        cell_below = {i:[] for i in cells_index}
        for index,alist in cell_below.items():
            alist += find_cell_behind(self.cdg,index)

        constraints_count = {i:[] for i in cells_index}
        for cell in cells_index:
            for below_cell in cell_below[cell]:
                producers = [producer for ce in self.cell_map for producer in ce.tmp_producers if ce.index == cell]
                consumers = [consumer for ce in self.cell_map for consumer in ce.other_consumers if ce.index == below_cell]
                if any(c in producers for c in consumers):
                    constraints_count[cell] += [below_cell]

        return constraints_count







if __name__ == "__main__":
    print("CDG Analyzer")