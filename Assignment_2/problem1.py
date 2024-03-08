import matplotlib as plt
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
        - label: string - label of the node
        - colour: integer - number representing the colour of the node, could change to colour 
                            or have colours corresponding to integers
        - neighbours: list/array-like - list of immediate neighbours

    ## Functions
        - __init__ : constructor - generates a node with a given label and no colour
        - __eq__ : equality operator for the ability to create nx.graphs directly using a list of these objects
        - __hash__ : hash function for the ability to create nx.graphs directly using a list of these objects
        - change_colour: change the colour of the node to the given number
        - get_colour: return the colour of the node
        - get_neighbours: return the list of neighbours
    """

    def __init__(self, label: str):
        self.label = label

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.label == other.label
        return False

    def __hash__(self) -> int:
        return hash(self.label)

    def change_colour(self):
        """change the colour of the node to the given number"""
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
        - first generate a hard-coded trivial 4-node graph
        - figure out what type of graph to generate
            - could do different types depending on what we want, for demonstration of successful approach
        - figure out what parameters to pass in
    """
    pass


def min_colours(g: nx.Graph):
    """Finds the expected minimum number of colours for any given graph"""
    pass


def fitness_function(g: nx.Graph):
    """
    Fitness function of the whole graph

    Error of number of conflicts or contstraints. count constraints and give it a score
    """
    pass


# main algorithm, can figure out how to approach problem 2 later, make a new file if needed


def problem1():
    """
    This is the main function / algorithm for problem 1.

    Made this to have a new thing to write labeleas down in

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
    pass
