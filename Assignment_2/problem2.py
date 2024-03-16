import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import sys
import os

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

    def __init__(self, id: str, personality: int = None):
        self.id = id
        self.colour = None
        self.known_colours = []
        self.neighbours = []
        self.personality = personality

    def communicate(self):
        """
        Communicate with neighbour

        Goes through neighbours to check for conflicts
        Following different rules depending on personality type
        """
        for neighbour in self.neighbours:
            if self.colour != neighbour.get_colour():  # no clash
                pass
            else:  # clash
                neighbour_personality = neighbour.get_personality()
                self.check_available_colours()
                neighbour.check_available_colours()
                if self.personality == neighbour_personality:  # clashing personality
                    # if both has available colours
                    if self.available_colours != []:
                        self.change_colour_available(
                            neighbour.get_unavailable_colours())
                        break
                    elif neighbour.available_colours != []:
                        neighbour.change_colour_available(
                            self.unavailable_colours)
                        break
                    else:
                        self.change_colour_random()
                        neighbour.change_colour_random()
                        break
                elif self.personality > neighbour_personality:  # self aggressive and neighbour passive
                    # passive node changes colour
                    if self.available_colours != [] and neighbour.available_colours != []:
                        neighbour.change_colour_available(
                            self.unavailable_colours)
                        break
                    else:
                        neighbour.change_colour_random()
                        break
                else:  # self passive and neighbour aggressive
                    # self changes colour
                    if self.available_colours != [] and neighbour.available_colours != []:
                        self.change_colour_available(
                            neighbour.get_unavailable_colours())
                        break
                    else:
                        self.change_colour_random()
                        break

    def check_available_colours(self):
        """Checking colours available and unavailable in the neighbourhood for the node to change to"""
        self.unavailable_colours = [n.get_colour() for n in self.neighbours]
        self.available_colours = [
            c for c in self.known_colours if c not in self.unavailable_colours]

    def change_colour_random(self):
        """Change colour to a random colour in known list"""
        new_colour = random.choice(self.known_colours)
        self.set_colour(new_colour)

    def change_colour_available(self, neighbour_unavailable_colours: list = None):
        """Change colour to random in given list of available colours"""
        # find common colours between available colours and neighbours unavailable colours
        if neighbour_unavailable_colours is not None:
            common_colours = [
                c for c in self.available_colours if c in neighbour_unavailable_colours]
            # if common colours exist, pick one
            if common_colours != []:
                new_colour = random.choice(common_colours)
                self.set_colour(new_colour)
            # if no common colours, pick a random colour from the available colours
            else:
                new_colour = random.choice(self.available_colours)
                self.set_colour(new_colour)
        # if neighbour_unavailable_colours is None
        else:
            new_colour = random.choice(self.available_colours)
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

    def get_unavailable_colours(self) -> list:
        """Returns unavailable colours in the neighbourhood"""
        return self.unavailable_colours

    def get_personality(self) -> int:
        """Returns personality type of the node"""
        return self.personality

    def get_id(self) -> str:
        return self.id

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self):
        return f"Node(id={self.id}, colour={self.colour}, personality={self.personality})"

    def __str__(self):
        return f"Node ID: {self.id}, Colour: {self.colour}, Personality: {'Aggressive' if self.personality == 1 else 'Passive'}"


# helper functions

def generate_graph(num_nodes: int = None, num_edges: int = None, p: int = 0.1, aggro_percentage: float = 0.5):
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
        G_small_world = nx.watts_strogatz_graph(num_nodes, num_edges, p)
        # nodes = [Node(str(i)) for i in range(num_nodes)]
        # create list of nodes, using aggro_percentage
        nodes = []
        for i in range(num_nodes):
            if random.random() < aggro_percentage:
                nodes.append(Node(str(i), 0))
            else:
                nodes.append(Node(str(i), 1))
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
        if node.get_colour() == neighbour.get_colour():
            conflicts += 1  # increment counter
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


def init_nodes(g: nx.Graph):
    """
    Function to give graph a random colouring from the given list of colours, 
    as well as updating each node with their neighbours.

    ## Parameters
    - g: nx.Graph - graph to be coloured
    - colours: list - list of colours to be used for the graph
    """
    colours_list = np.random.choice(global_colours_list, min_colours)

    # assign random colours to nodes from the list of colours
    for node in g.nodes():
        colour = random.choice(colours_list)
        node.set_colour(colour)
        node.set_known_colours(colours_list)
        # update neighbours
        # add all connected nodes to neighbours
        # Get actual node references from the graph
        neighbours = [n for n in g.neighbors(node)]
        node.set_neighbours(neighbours)
        # neighbours = g.neighbors(node)
        # node.add_neighbour(neighbour for neighbour in neighbours)


def algorithm(graph: nx.Graph, num_iterations: int, graph_show: bool = True):
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
        if graph_show:
            if num_iterations <= 100:
                plt.pause(0.05)
            else:
                plt.pause(0.025)

        # get fitness
        fitness = fitness_function(graph)
        print(f"Iteration: {i}, Fitness: {fitness}")
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
            node.communicate()

    return fitness_list


if __name__ == '__main__':
    for i in range(10):
        num_nodes = int(sys.argv[1])
        num_edges = int(sys.argv[2])
        aggro_percentage = float(sys.argv[3])
        graph = generate_graph(num_nodes, num_edges,
                               0.1, aggro_percentage)
        min_colours = minimum_colours(graph)
        # initialise graph with colours
        init_nodes(graph)

        # make empty plot to host graph plot and fitness plot
        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        fitness = algorithm(graph, 500, False)

        # plot fitness over time and add to the same figure
        # ensure no overlapping of plots
        ax2 = fig.add_subplot(2, 1, 2)
        ax2.plot(fitness)
        ax2.set_title("Fitness over time")
        ax2.set_xlabel("Iterations")
        ax2.set_ylabel("Fitness")
        ax2.grid(True)
        # save the plot to images folder
        # relative to the script
        currdir = os.path.dirname(__file__)
        image_path = os.path.join(currdir, "Images/prob2")
        plt.savefig(
            f"{image_path}/{num_nodes}n_{num_edges}e_{int(aggro_percentage*100)}aggro_{i}.png")
        plt.close()
