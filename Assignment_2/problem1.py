import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

global_colours_list = [
    '#FFFFFF', '#C0C0C0', '#808080', '#000000', '#FF0000', '#800000',
    '#FFFF00', '#808000', '#00FF00', '#008000', '#00FFFF', '#008080',
    '#0000FF', '#000080', '#FF00FF', '#800080', '#baeed2', '#6dacfc',
    '#a83a18', '#af4113', '#481288', '#715f3c', '#e0f804', '#fb9274',
    '#a7c99e', '#38db5a'
]


class Node():
    """
    Object to represent a node in a graph.

    - Agents, or nodes, only have local knowledge.
    - They have a set of rules.
    - They can only communicate with their neighbours.

    ## Attributes
        - id: string - id of the node
        - colour: integer - number representing the colour of the node, could change to colour 
                            or have colours corresponding to integers
        - neighbours: list/array-like - list of immediate neighbours

    ## Functions
        - __init__ : constructor - generates a node with a given id and no colour
        - __eq__ : equality operator for the ability to create nx.graphs directly using a list of these objects
        - __hash__ : hash function for the ability to create nx.graphs directly using a list of these objects
        - change_colour: change the colour of the node to the given number
        - get_colour: return the colour of the node
        - get_neighbours: return the list of neighbours
    """

    def __init__(self, id: str):
        self.id = id
        self.colour = None
        self.known_colours = []
        self.neighbours = []

    def communicate(self):
        """
        Communicate with neighbour

        Goes through neighbours to check for conflicts
        If conflict exist, both nodes change to a random available colour
        Else move on
        """
        for neighbour in self.neighbours:
            print(f"Node {self.id} colour: {self.colour}")
            print(f"Node {neighbour.id} colour: {neighbour.get_colour()}")
            if self.colour == neighbour.get_colour():
                print("Conflict detected! Changing colours...")
                self.change_colour()
                neighbour.change_colour()
            else:
                pass

    def change_colour(self):
        """Change colour to a random colour in known list"""
        print(f"Number of colours: {len(self.known_colours)}")
        new_colour = random.choice(self.known_colours)
        print(
            f"Changing colour of node {self.id} from {self.colour} to {new_colour}", end='')
        self.set_colour(new_colour)

    def set_colour(self, colour: str):
        """Set the colour of the node"""
        self.colour = colour

    def set_known_colours(self, known_colours: list):
        """Set the list of known colours"""
        self.known_colours = known_colours

    def set_neighbours(self, neighbours: list):
        """Add a neighbour to the list of neighbours"""
        self.neighbours = list(neighbours)

    def add_neighbour(self, neighbour):
        """Add a neighbour to the list of neighbours"""
        self.neighbours.append(Node(neighbour))

    def get_colour(self) -> str:
        """Returns current colour of the node"""
        return self.colour

    def get_neighbours(self) -> list:
        """Returns neighbours of the node"""
        return self.neighbours

    def get_id(self) -> str:
        return self.id

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)


# helper functions

def generate_graph(num_nodes: int = None, num_edges: int = None, seed: int = 0):
    """
    Function to generate a graph using networkx.

    TODO: 
        - figure out what type of graph to generate
            - could do different types depending on what we want, for demonstration of successful approach
        - figure out what parameters to pass in
    """
    # construct an empty graph object
    G = nx.Graph()

    if num_nodes is None or num_edges is None:
        # make trivial graph if no parameters passed in
        nodes = [Node(str(i)) for i in range(4)]
        for node in nodes:
            G.add_node(node)
        # add edges
        G.add_edge(nodes[0], nodes[1])
        G.add_edge(nodes[1], nodes[2])
        G.add_edge(nodes[2], nodes[3])
        G.add_edge(nodes[3], nodes[0])
    else:
        # small world graph
        if seed is not None:
            random.seed(seed)
        G_small_world = nx.watts_strogatz_graph(num_nodes, num_edges, seed)
        nodes = [Node(str(i)) for i in range(num_nodes)]
        for node in nodes:
            G.add_node(node)
        for edge in G_small_world.edges():
            node1, node2 = edge[0], edge[1]
            # if the nodes are not in the graph, they will be added!!!
            # a.k.a. they are being duplicated because the graph does not have a reference to the nodes
            G.add_edge(nodes[int(node1)], nodes[int(node2)])
    return G


def minimum_colours(g: nx.Graph):
    """Finds the expected minimum number of colours for any given graph"""
    graph_colouring = nx.coloring.greedy_color(g, strategy='largest_first')
    min_colours = max(graph_colouring.values())+1
    print(f"Minimum number of colours required: {min_colours}")
    return min_colours


def node_fitmess(node: Node):
    # count number of conflicts
    conflicts = 0  # init counter
    for neighbour in node.get_neighbours():  # iterate through neighbours
        # check for collision of colours
        print(
            f"Node colour: {node.get_colour()}, Neighbour colour: {neighbour.get_colour()}")
        if node.get_colour() == neighbour.get_colour():
            conflicts += 1  # increment counter
            print(f"Conflict count: {conflicts}")
    return conflicts


def fitness_function(g: nx.Graph):
    """
    Fitness function of the whole graph

    Returns the number of conflicts in the graph
    """
    # count number of global conflicts
    conflicts = 0
    for node in g.nodes:
        conflicts += node_fitmess(node)
    return conflicts


def init_nodes(g: nx.Graph, colours: list):
    """
    Function to give graph a random colouring from the given list of colours, 
    as well as updating each node with their neighbours.

    ## Parameters
    - g: nx.Graph - graph to be coloured
    - colours: list - list of colours to be used for the graph
    """
    # assign random colours to nodes from the list of colours
    for node in g.nodes():
        colour = random.choice(colours)
        node.set_colour(colour)
        node.set_known_colours(colours)
        # update neighbours
        # add all connected nodes to neighbours
        # Get actual node references from the graph
        neighbours = [n for n in g.neighbors(node)]
        node.set_neighbours(neighbours)
        # neighbours = g.neighbors(node)
        # node.add_neighbour(neighbour for neighbour in neighbours)


def algorithm(graph: nx.Graph, num_iterations: int):
    """
    This is the main algorithm for problem 1.

    ## Parameters
    - graph - nx.Graph - graph to be coloured
    - num_iterations: int - number of iterations to run the algorithm for
    - min_colour_num: int - minimum number of colours required for the graph - can be used as the convergence measure
    """

    # make list to store fitness values
    fitness_list = []

    # get initial fitness of the graph
    best_fitness = fitness_function(graph)
    print("Initial fitness:", best_fitness)
    fitness_list.append(best_fitness)

    # algorithm
    for i in range(num_iterations):
        # visualisation
        ids = {node: node.id for node in graph.nodes()}
        pos = nx.spring_layout(graph)

        plt.clf()
        # update graph with new colours
        nx.draw(graph, pos, with_labels=True, labels=ids,
                node_color=[node.get_colour() for node in graph.nodes()])
        plt.pause(1)

        # get fitness
        fitness = fitness_function(graph)
        if fitness < best_fitness:
            best_fitness = fitness
            print("New best fitness:", best_fitness)
        fitness_list.append(fitness)

        if fitness == 0:
            print(f"Convergence reached!!\nTook {i} iterations")
            return fitness_list

        # loop through nodes
        # get them all to communicate with their neighbours
        for node in graph.nodes():
            # print neighbours
            print(f"Node {node.id} neighbours: {node.get_neighbours()}")
            node.communicate()

        # plot the graph as well as the fitness on the same figure
        # plt.plot(i, fitness, 'ro')

    return fitness_list


if __name__ == '__main__':
    """
    Main function

    Generates a graph, finds out minimum number of colours required for the graph and then runs the algorithm.

    #### Procedure (idea)
    1. Generate nodes
    2. Generate graph using nodes
    3. Find out min_colours for said graph
    4. Make number available to graph
    5. Run main algorithm (?) till either convergence or iterations reached
    """
    # trivial graph to demonstrate algorithm is functional
    # graph = generate_graph()
    graph = generate_graph(10, 5, 0)
    min_colours = minimum_colours(graph)
    colours_list = np.random.choice(global_colours_list, min_colours)
    # initialise graph with colours
    init_nodes(graph, colours_list)

    # make empty plot to host updating graph
    fig, ax = plt.subplots()
    fitness = algorithm(graph, 10)

    # plot fitness over time and add to the same figure
    plt.plot(fitness)
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')
    plt.title('Fitness over time')
    plt.show()
