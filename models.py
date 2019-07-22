import json


class Node:

    def __init__(self, info_list: list, root: bool = False):
        self.root = root
        self.childs = []
        self.number_children = info_list.pop(0)
        self.amount_of_metada = info_list.pop(0)
        self.generate_children(info_list)
        self.metadata = [info_list.pop(0) for _ in range(self.amount_of_metada)]

    def generate_children(self, info_list):
        self.children = [Node(info_list) for _ in range(self.number_children)]

    def get_dict(self):
        data = {"number of children": self.number_children,
                "amount of metadata": self.amount_of_metada,
                "metadata": self.metadata,
                "childrens": [child.get_dict() for child in self.children]}
        if self.root:
            data["total"] = self.get_total()

        return data

    def get_total(self):
        return sum(self.metadata) + sum(child.get_total() for child in self.children)

    def print_tree(self):
        print(json.dumps(self.get_dict()))
