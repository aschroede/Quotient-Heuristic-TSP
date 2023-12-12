from graph import NetworkGraph
from node import Node
import math

class utils:

    @classmethod
    def read_point_set(cls, file) -> NetworkGraph: 

        #graph = NetworkGraph()
        nodeList = []

        with open(file, "r") as point_set:
            
            for index, line in enumerate(point_set.readlines()):

                # Each line comes in as two number: 100 100 (x, y)
                numbers = line.split()

                x = int(numbers[0])
                y = int(numbers[1])

                node = Node(x, y, index+1)
                nodeList.append(node)

        return nodeList
    

    @classmethod
    def quotient_heuristic(cls, node_list: list, initial_node) -> list:

        available = node_list.copy()
        available.remove(initial_node)
        current = initial_node
        visited = [initial_node]

        
        while len(available) > 1:

            list_for_centroid = available
            centroid_coords = utils.calculate_centroid(list_for_centroid)
            centroid = Node(centroid_coords[0], centroid_coords[1], -1) 
            
            quotient_costs = {}
            for node in available:

                node_dist = utils.calculate_distance(node, current)
                centroid_dist = utils.calculate_distance (node, centroid)

                if centroid_dist != 0:
                    quotient_costs[node]=node_dist/centroid_dist
                else:
                    quotient_costs[node]=node_dist/0.0001

            next_node = min(quotient_costs.items(), key=lambda x: x[1])[0]

            available.remove(next_node)
            visited.append(next_node)
            current = next_node
        
        visited.append(available[0])

        return visited

    @classmethod
    def calculate_distance(cls, node1: Node, node2: Node):

        distance = math.sqrt((node2.x - node1.x)**2 + (node2.y - node1.y)**2)
        return distance

    @classmethod
    def calculate_centroid(cls, node_list: list) -> tuple:
        
        x_sum = 0
        y_sum = 0

        for node in node_list:
            x_sum += node.x
            y_sum += node.y
        
        x_avg, y_avg = x_sum/len(node_list), y_sum/len(node_list)

        return (x_avg, y_avg)


