from models import Node

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_list = f.read().strip().split(" ")
        results = list(map(int, input_list))
        root = Node(results, True)
        root.print_tree()
