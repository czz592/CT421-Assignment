
<div align="center">

<h1> CT421 Assignment 2 </h1>

<h2> Leo Chui, Aoife Mulligan </h2>

<h3><a href="https://www.github.com/czz592/ct421-assignment/">GitHub Repo</a></h3>

</div>

# Development Approach

Our development process began by discussing the assignment. We first discussed the assignment to see each other's interpretation regarding the assignment and brainstorm to come up with how to approach part 1 and ideas for part 2, and collected all of our ideas into a text file to look back at during development.

After a discussion regarding multi-agent systems and graph colouring, and how the two can come together, we decided to take an OOP approach, by creating a ``Node`` class that represents the agents. 

The basic idea is to use ``Networkx``, the Python package for everything networks science and graphs, to create graphs and populate them with instances of the Node class, which will be our agents.

To best mimic the decentralised computation, the main algorithm only calls the ``communicate()`` function of nodes. The nodes then handles everything else.

The code for problem 1 and problem 2 are mostly the same, starting with the class for ``Node``. In order for ``Networkx`` to be able to create graphs using our custom ``Node`` class, it implements some functions that serves no direct purpose for the assignment. The class then has various getters and setters, for variables such as its colour and neighbours. 

In the class, the main function of interest in the class is ``communicate()``. This function is the 

# Part 1

## Initial Graph

We decided to start this assignment by first creating a small graph with 4 nodes and 4 edges, and trying to write an algorithm that could colour it using two colours.

![Initial Four Node Graph](/Images/initial-4nodes.jpg)

The mutation function randomly changed nodes to a colour that worked. Initially, we had tried changing only the poorest performing node, but this would only reach a fitness of 0 if it started at 0, otherwise it would oscillate between a fitness of 4 and a fitness of 8.

We had two methods of measuring fitness: 
1. Individual fitness of a node, by counting the number of conflicting neighbours. Best fitness would be 0, worst would be 2.
2. Calculating the overall fitness of the graph by getting the sum of the fitnesses of each node. The best would be 0, worst would be 8.

This meant that, the initial fitness function was swapping between having all 4 nodes coloured, and each node having a single conflict for each node.
I changed this, so that it would randomly choose a node to mutate, and it improved the ability to find the optimal solution.

The resulting coloured graph looked like:

![Coloured Four Node Graph](/Images/colored-4nodes.jpg)

## Small-World Graphs

We decided to use a small world graph to represent this problem, because small-world graphs are reminiscent of human social networks, and the problem we are tackling concerns a 'society' of sorts.

### Graph 1:


