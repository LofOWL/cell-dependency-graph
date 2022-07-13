
class SnippetCode:

    def __init__(self,mapping):
        self.hashmap = {i.index:i for i in mapping}

    def getSnippet(self,cellIndex):
        cell = self.hashmap.get(cellIndex)
        if not cell: return False
        cellBefore = list(filter(lambda x: x < cellIndex,list(self.hashmap.keys())))
        cellBefore.reverse()
        combinations = self.dfs(cellBefore,cell.consumers)
        return [[cellIndex]+combination for combination in combinations] 

    def dfs(self,cellBefore,consumers):
        if not consumers:
            return [[]]
        if not cellBefore: 
            return [[]] if not consumers else [consumers]

        l = []
        for i in range(0,len(cellBefore)):
            cell = self.hashmap.get(cellBefore[i])
            filter_consumers = [consumer for consumer in consumers if consumer not in cell.producers]
            if len(filter_consumers) != len(consumers):
                for p in self.dfs(cellBefore[i+1:],cell.consumers+filter_consumers):
                    l.append([cell.index]+p)
        return l
