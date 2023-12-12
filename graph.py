from node import Node

class NetworkGraph:

    def __init__(self) -> None:
        self.nodes = {}

    def add_node(self, node: Node):

        if node.id not in self.nodes.keys():
            self.nodes[node.id] = node

    def remove_node(self, node: Node):

        if node.id in self.nodes.keys():
            self.nodes.pop(node.id)

    def get_all_nodes(self):
        return self.nodes