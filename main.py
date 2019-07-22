from models import Node

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_list = f.read().split(" ")
        results = list(map(int, input_list))
        root = Node(results)
        root.PrintTree()
