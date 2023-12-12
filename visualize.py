import networkx as nx
import matplotlib.pyplot as plt
from graph import NetworkGraph


def visualize_nodes(nodes: list, tour: list):
    
    G = nx.Graph()

    # Add nodes to the graph
    for node in nodes:
        G.add_node(node.id, pos=(node.x, node.y))

    # Add edges based on the TSP tour
    for i in range(len(tour) - 1):
        G.add_edge(tour[i].id, tour[i + 1].id)

    G.add_edge(tour[-1].id, tour[0].id)  # Close the loop

    pos = nx.get_node_attributes(G, 'pos')
    
    # Draw nodes
    #nx.draw_networkx_nodes(G, pos, node_size=200, node_color='blue', label=True)

    nx.draw(G, pos, with_labels = True, node_size=200, node_color='green')
    
    # Highlight TSP tour in red
    nx.draw_networkx_edges(G, pos, edgelist=[(tour[i].id, tour[i + 1].id) for i in range(len(tour) - 1)],
                        edge_color='red', width=2)
    
    nx.draw_networkx_edges(G, pos, edgelist=[(tour[-1].id, tour[0].id)], edge_color='red', width=2)

    # Invert the Y-axis
    plt.gca().invert_yaxis()
    #plt.gca().invert_xaxis()

    plt.axis('off')
    plt.show()

# Example usage
# points = [(500, 100), (500, 6200), (10000, 6200), (10000, 100), (4350, 6201), (5220, 6203), (6120, 6202), (8000,6201), (5200, 4000),
#           (5200, 4500), (5200, 5000), (5200, 5500), (5200, 6000), (6210, 4245)]
# tour = [0, 1, 2, 3, 4, 5]  # Example tour (replace with your algorithm's result)
# visualize_tsp(points, tour)
