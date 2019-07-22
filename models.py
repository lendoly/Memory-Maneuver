from generators import next_letter

generator = next_letter()


class Node:

    def __init__(self, info_list):

        self.childs = []
        self.node_name = next(generator)
        self.number_childs = info_list[0]
        self.amount_of_metada = info_list[1]
        self.metadata = info_list[-self.amount_of_metada:]
        self.generate_childrens(info_list[2:-self.amount_of_metada])

    def generate_childrens(self, info_list):
        grow = len(info_list) // self.number_childs
        for i in range(self.number_childs):
            actual = i * grow
            print(f"number of childs: {info_list[actual]}, "
                  f"number of metadata: {info_list[actual + 1]}, "
                  f"list= {info_list[actual + 3: actual + grow]}")

    def PrintTree(self):
        print(f"Node {self.node_name}, "
              f"number of childs: {self.number_childs}, "
              f"amount of metadata: {self.amount_of_metada}, "
              f"metadata: {self.metadata}, childs: {self.childs}")
