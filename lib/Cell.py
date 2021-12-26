

class Cell:

    def __init__(self,item):
        self.index = item[0]
        self.producers = item[1][0]
        self.consumers = item[1][1]
        self.before_producers = list()
        self.tmp_producers = [producer for producer in self.producers if producer not in self.before_producers]
        self.other_consumers = [consumer for consumer in self.consumers if consumer not in self.tmp_producers]

    def set_before_producers(self,alist):
        self.before_producers = alist
        self.tmp_producers = [producer for producer in self.producers if producer not in self.before_producers]
        self.other_consumers = [consumer for consumer in self.consumers if consumer not in self.tmp_producers]

    def __str__(self):
        return f"{self.index} \nP:{self.producers} \nC:{self.consumers} \nCC:{self.other_consumers} \nBP:{self.before_producers}"