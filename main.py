from utils import utils
from graph import NetworkGraph
from visualize import visualize_nodes


def main():

    file = "./PointSets/dantzig.txt"

    nodelist = utils.read_point_set(file)

    tour = utils.quotient_heuristic(nodelist, nodelist[0])

    visualize_nodes(nodelist, tour)

    #print(graph.get_all_nodes())





if __name__ == '__main__':
    main()