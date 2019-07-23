import copy

from models import Node

EXAMPLE_INPUT = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2] 

def test_node_constructor_root_true():
    copy_list = copy.deepcopy(EXAMPLE_INPUT)
    new_node = Node(copy_list, True)

    assert new_node.root
    assert new_node.number_children == EXAMPLE_INPUT[0]
    assert new_node.amount_of_metada == EXAMPLE_INPUT[1]
    assert new_node.metadata == EXAMPLE_INPUT[-3:]

def test_node_constructor_root_false():
    copy_list = copy.deepcopy(EXAMPLE_INPUT)
    new_node = Node(copy_list, False)

    assert not new_node.root
    assert new_node.number_children == EXAMPLE_INPUT[0]
    assert new_node.amount_of_metada == EXAMPLE_INPUT[1]
    assert new_node.metadata == EXAMPLE_INPUT[-3:]

def test_node_get_total():
    copy_list = copy.deepcopy(EXAMPLE_INPUT)
    new_node = Node(copy_list, True)
    assert new_node.get_total() == 138

def test_node_get_dict():
    copy_list = copy.deepcopy(EXAMPLE_INPUT)
    new_node = Node(copy_list, True)
    node_dict = new_node._get_dict()
    assert node_dict.get("number of children") == EXAMPLE_INPUT[0]
    assert node_dict.get("metadata") == EXAMPLE_INPUT[-3:]
    assert node_dict.get("amount of metadata") == EXAMPLE_INPUT[1]
    assert node_dict.get("total") == 138
    assert len(node_dict.get("childrens")) == EXAMPLE_INPUT[0]


def test_generate_children():
    copy_list = copy.deepcopy(EXAMPLE_INPUT)
    new_node = Node(copy_list, True)
    assert len(new_node.children) == EXAMPLE_INPUT[0]
    node_b = new_node.children[0]
    assert node_b.number_children == EXAMPLE_INPUT[2]
    assert len(node_b.children) == EXAMPLE_INPUT[2]
    assert node_b.amount_of_metada == EXAMPLE_INPUT[3]
    assert node_b.metadata == EXAMPLE_INPUT[4:4 + EXAMPLE_INPUT[3]]

    node_c = new_node.children[1]
    assert node_c.number_children == EXAMPLE_INPUT[7]
    assert node_c.amount_of_metada == EXAMPLE_INPUT[8]
    assert len(node_c.children) == EXAMPLE_INPUT[7]
    assert node_c.metadata == EXAMPLE_INPUT[12: 12 + EXAMPLE_INPUT[7]]


    node_d = node_c.children[0]
    assert node_d.number_children == EXAMPLE_INPUT[9]
    assert len(node_d.children) == EXAMPLE_INPUT[9]
    assert node_d.amount_of_metada == EXAMPLE_INPUT[10]
    assert node_d.metadata == EXAMPLE_INPUT[11: 11 + EXAMPLE_INPUT[10]]


