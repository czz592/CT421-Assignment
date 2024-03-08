import matplotlib as plt
import networkx as nx
import numpy as np
import random


class node():
    """
    Object to represent a node in a graph.

    - Agents, or nodes, only have local knowledge.
    - They have a set of rules.
    - They can only communicate with their neighbours.

    ## Attributes
        - label: string - id of the node
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

    def __init__(self):
        pass

    def __eq__(self, __value: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass

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
        - figure out what type of graph to generate
            - could do different types depending on what we want, for demonstration of successful approach
        - figure out what parameters to pass in
    """
    pass

# main algorithm, can figure out how to approach problem 2 later, make a new file if needed


def problem1():
    """
    This is the main function / algorithm for problem 1.

    Made this to have a new thing to write ideas down in

    ## Structure

    #### Functions
    - minimum_colour function to return minimum number of colours required for any given networkx graph
    - colour_init function to give graph a random colouring

    #### 
    """
    pass
