
<div align="center">

<h1> CT421 Assignment 2 </h1>

<h2> Leo Chui (20343266), Aoife Mulligan (20307646)</h2>

<h3><a href="https://www.github.com/czz592/ct421-assignment/">GitHub Repo</a></h3>

</div>

# Development Approach

### Brainstorming

Our development process began by discussing the assignment. We first discussed the assignment to see each other's interpretation regarding the assignment and brainstorm to come up with how to approach part 1 and ideas for part 2, and collected all of our ideas into a text file to look back at during development.

After a discussion regarding multi-agent systems and graph colouring, and how the two can come together, we decided to take an OOP approach, by creating a ``Node`` class that represents the agents. 

### Structure of Code

Our solutions for the assignment are split based on the problems. Both Python modules contain mostly the same code: 
- a definition for a ``Node`` class
- ``generate_graph()``, a graph generator function that generates either a trivial, 4-node, 4-edge graph if no parameters are passed in, or a Small-World graph with $n$ nodes and $m$ edges
- ``minimum_colours()``, a function to determine the theoretical minimum chromatic colour of a graph
- ``node_fitness()`` and ``fitness_function``, first of which calculates conflicts on the individual level, and the latter is a fitness function that calculates the number of conflicts in the entire graph
- ``init_nodes()``, a function that gives graph a random colouring from the global list of colours, gives all nodes a list of colours that is ``min_colour_num`` long, and updates all nodes with their neighbours
- ``algorithm()``, the main function for both problems. It calculates the fitness of the graph at any given iteration, checks whether it has converged or not, plots the graph, and gets all nodes to communicate with their neighbours.

The basic idea is to use ``Networkx``, the Python package for everything networks science and graphs, to create graphs and populate them with instances of the ``Node`` class, which will be our agents.

#### Node

All nodes maintain two lists, ``neighbours``, which are nodes they are connected to via an edge in the graph, and ``known_colours``, a list of colours that is sufficiently sized to reach a minimum graph colouring. 

In order for ``Networkx`` to be able to create graphs using our custom ``Node`` class, it implements some functions that serves no direct purpose for the assignment (\_\_eq\_\_, \_\_hash\_\_). The class then has various getters and setters, for variables such as its colour and neighbours. 

In the class, the main function of interest in the class is ``communicate()``. General idea of the function is that the node will check for colour conflicts with all of its neighbours. 
- In the case of no-conflicts, nothing occurs. 
- In the case of a conflict, both nodes will check for their respective unavailable and available colours
	- ``unavailable-colours``, list of colours of the neighbours
	- ``available_colours``, list of colours in the ``known_colours`` list that are not in ``unavailable-colours``

Based on whether ``available_colours`` of either node 1 or 2 is empty, the node with the non_empty ``available_colours`` will change colour to one in that list, or both will change to a random colour in ``known_colours``.

This is slightly different in problem 2, which will be discussed in further details in a later section.

### Graphs

For both problems, we begin testing our the validity of our approach by using a small graph on 4 nodes, $1,2,3, \text{ and }4$, and the edges list are as follows: $(1,2), (2,3), (3,4), \text{ and } (4,1)$. The minimum colouring for such a graph is 2.

![[initial_graph_prob1.png]]

The topology we chose was Small-World. 

![[10node_6edge_0.png]]

# Part 1

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



# Appendix