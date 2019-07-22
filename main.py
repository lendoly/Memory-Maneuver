from models import Node

if __name__ == "__main__":
    # Opening file and read it
    with open("input.txt", "r") as f:
        try:
            input_list = f.read().strip().split(" ")
            results = list(map(int, input_list))
            root = Node(results, True)
            root.print_tree()
        except  ValueError as e:
            print("Invalid input, probably there are letters on it")
