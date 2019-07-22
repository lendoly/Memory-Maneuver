import json


class Node:
    """Class that simbolize a Node of a Tree.

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        root (bool): Indicates if is the root Node of a Tree or not
        number_children (int): Number of children for a Node 
        amount_of_metada (int): Number of metadat on the node 
        children (list): List of Nodes which are the children of the Node
        metadata (list): List of Integers with the metada for the Node 
    """
    def __init__(self, info_list: list, root: bool = False):
        """Constructor for the Node

        Note:
            Do not set root to True on the Tree generation

        Args:
            info_list (list): list of integers with the input
            root (bool): indicates if is a ROOT node or not, default to False

        """
        self.root = root
        self.number_children = info_list.pop(0)
        self.amount_of_metada = info_list.pop(0)
        self.generate_children(info_list)
        self.metadata = [info_list.pop(0)
                         for _ in range(self.amount_of_metada)]

    def generate_children(self, info_list):
        """Class method that will generate the chidlren for the Node

        Args:
            info_list: The rest of the list to generate children.

        Returns:
            None

        """
        #: list of Node: caontain the children for the current node
        self.children = [Node(info_list) for _ in range(self.number_children)]

    def get_dict(self):
        """Class method that will generate the children for the Node
        
        Args:
            info_list: The rest of the list to generate children.

        Returns:
            dict with the information for the 

        """
        data = {"number of children": self.number_children,
                "amount of metadata": self.amount_of_metada,
                "metadata": self.metadata,
                "childrens": [child.get_dict() for child in self.children]}
        if self.root:
            data["total"] = self.get_total()

        return data

    def get_total(self):
        """Class method that will sum the current metada and add the
        sum of the children's metadata
        
        Returns:
            total amount of the sum of all the metadata 

        """

        return sum(self.metadata) + sum(child.get_total()
                                        for child in self.children)

    def print_tree(self):
        """Print in JSON format the tree from the current Node
        Returns:
            None
        """
        print(json.dumps(self.get_dict()))
