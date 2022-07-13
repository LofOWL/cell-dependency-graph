from AST import ASTProvider

bug_elements = ['!','%']

class Cell:

    def __init__(self):
        self.index = -1
        self.producers = list()
        self.consumers = list()

    def set_producers_consumers(self,producers,consumers):
        self.producers = producers
        self.consumers = consumers

    def set_index(self,index):
        self.index = index

    def __str__(self):
        return f"{self.index} \nP:{self.producers} \nC:{self.consumers}"


if __name__ == "__main__":
    #notebook = "/Users/root1/Desktop/cell-dependency-graph/example/test.ipynb"
    c = Cell()
    c.generate_producers_consumers(['train_data = pd.get_dummies(train_data, columns=["Embarked"])'])