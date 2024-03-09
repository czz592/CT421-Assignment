import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random


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

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)

    def change_colour(self):
        """change the colour of the node to the given colour"""
        pass

    def get_colour(self):
        pass

    def get_neighbours(self):
        pass

# helper functions


def generate_graph():
    """
    Function to generate a graph using networkx.

    TODO: 
        - figure out what type of graph to generate
            - could do different types depending on what we want, for demonstration of successful approach
        - figure out what parameters to pass in
    """
    # construct an empty graph object
    G = nx.Graph()

    # make list of nodes
    # TODO: change to make non-trivial graph
    # based on parameters
    for i in range(1, 5):
        # create node object with i
        G.add_node(Node(str(i)))

    # add edges
    G.add_edge(Node('1'), Node('2'))
    G.add_edge(Node('2'), Node('3'))
    G.add_edge(Node('3'), Node('4'))
    G.add_edge(Node('4'), Node('1'))

    return G


def minimum_colours(g: nx.Graph):
    """Finds the expected minimum number of colours for any given graph"""
    graph_colouring = nx.coloring.greedy_color(g, strategy='largest_first')
    min_colours = max(graph_colouring.values()) + 1
    print("Minimum number of colours required: ", min_colours)
    return min_colours


def fitness_function(g: nx.Graph):
    """
    Fitness function of the whole graph

    Error of number of conflicts or contstraints. count constraints and give it a score
    """
    pass


# main algorithm, can figure out how to approach problem 2 later, make a new file if needed

global_colours_list = [
    '#FFFFFF', '#C0C0C0', '#808080', '#000000', '#FF0000', '#800000',
    '#FFFF00', '#808000', '#00FF00', '#008000', '#00FFFF', '#008080',
    '#0000FF', '#000080', '#FF00FF', '#800080', '#baeed2', '#6dacfc',
    '#a83a18', '#af4113', '#481288', '#715f3c', '#e0f804', '#fb9274',
    '#a7c99e', '#38db5a'
]


def problem1():
    """
    This is the main function / algorithm for problem 1.

    Made this to have a new thing to write ideas down in

    ## Structure

    #### Functions
    - minimum_colour function to return minimum number of colours required for any given networkx graph
    - colour_init function to give graph a random colouring

    #### Procedure (idea)
    1. Generate nodes
    2. Generate graph using nodes
    3. Find out min_colours for said graph
    4. Make number available to graph
    5. Run main algorithm (?) till either convergence or iterations reached
    """
    # create graph
    # TODO: change call to make non-trivial graph
    graph = generate_graph()

    # find minimum number of colours
    min_colours = minimum_colours(graph)
    colours = np.random.choice(global_colours_list, min_colours)
    print(colours)

    # draw graph
    ids = {node: node.id for node in graph.nodes()}
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, labels=ids,
            node_color=global_colours_list[0])
    plt.show()


if __name__ == '__main__':
    problem1()
