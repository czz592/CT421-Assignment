
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
- a definition for a ``Node`` class, which includes various OOP-related functions, colour-changing functions, ``communicate()``, and object functions like ``__eq__()`` and ``__hash__()``
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

Based on whether ``available_colours`` of either node 1 or 2 is empty, the node with the non-empty ``available_colours`` will change colour to one in that list, or both will change to a random colour in ``known_colours``.

This is slightly different in problem 2, which will be discussed in further details in its own section.

### Graphs

For both problems, we begin testing our the validity of our approach by using a small graph on 4 nodes, $1,2,3, \text{ and }4$, and the edges list are as follows: $(1,2), (2,3), (3,4), \text{ and } (4,1)$. The minimum colouring for such a graph is 2.

![[initial_graph_prob1.png]]

The topology we chose was Small-World. 

![[10node_6edge_0.png]]

# Part 1

27/30 converged runs suggests that the algorithm performs well. For the runs that did not converge, our theory is that the initialisation of the graph may sometimes mislead and give the graph a local optima of colouring, as during development, we had great difficulty reaching convergence even for a trivial 4-node graph when we randomly coloured the graph with only the minimum amount of colours needed.

## 10 Node 6 Degree

For a small-world graph with 10 nodes and 6 degrees, it reaches a minimum colouring 8 times out of 10. Below shows two runs for 1000 iterations, 1 success, 1 fail. More images can be found at the end of the report in the Appendix.

![[10node_6edge_0.png]]

![[10node_6edge_3.png]]


## 40 Node 6 Degree

Part 1 solution performed slightly better over 10 runs, reaching convergence 9 times.

![[40node_6edge_9.png]]

![[40node_6edge_0.png]]

## 40 Node 7 Degree

The solution again reached convergence 8 runs out of 10.

![[40node_7edge_9.png]]

![[40node_7edge_2.png]]


# Part 2

## Changes to Communicate

We decided to explore what effects may be present if nodes were given "personalities". The inspiration came when the network was interpreted as a network of people, and that the colouring was some sort of "negotiation" process. 

During our discussion for part 1, questions such as "should both nodes change colour at the same time?" or "which node would have precedence if they are not to change at the same time?" were raised, and an attempt to address those questions was to give nodes a personality.

A node can either be "Aggressive/Assertive" or "Passive". This is represented as an integer, either 0 representing *Passive*, or 1 representing *Aggressive*.

The ``personality`` affects the way nodes communicate, as thwe two types of personality has different "priority" when changing colours, and the new set of rules when communicating is listed below.

Assuming conflict, both check available colours and personalities. 

If personalities clash (both aggressive or both passive):

- if either node has available colours: the node with available colours will change
- else both change to random

Else, the aggressive node will tell the passive node to either change to an available colour, or a random colour, depending on whether or not their lists of available colours are empty or not.


To test the approach, we decided to stick with the 40 node, 6 degree, small-world graph. The numbers are of arbitrary choice. Below will compare the different percentages of aggressive nodes. Please note that the percentage of aggressive nodes are approximated, as the random function is used.

## 50% Aggressive



## 30% Aggressive



## 70% Aggressive



# Conclusion & Discussion



# Appendix

## Problem 1

### 10 Node 6 Degree

![[10node_6edge_0.png]]

![[10node_6edge_9.png]]

![[10node_6edge_8.png]]

![[10node_6edge_7.png]]

![[10node_6edge_6.png]]

![[10node_6edge_5.png]]

![[10node_6edge_4.png]]

![[10node_6edge_3.png]]

![[10node_6edge_2.png]]

![[10node_6edge_1.png]]



### 40 Node 6 Degree

![[40node_6edge_3.png]]

![[40node_6edge_2.png]]

![[40node_6edge_0.png]]

![[40node_6edge_1.png]]

![[40node_6edge_9.png]]

![[40node_6edge_8.png]]

![[40node_6edge_7.png]]

![[40node_6edge_6.png]]

![[40node_6edge_5.png]]

![[40node_6edge_4.png]]

### 40 Node 7 Degree

![[40node_7edge_0.png]]

![[40node_7edge_9.png]]

![[40node_7edge_8.png]]

![[40node_7edge_7.png]]

![[40node_7edge_6.png]]

![[40node_7edge_5.png]]

![[40node_7edge_4.png]]

![[40node_7edge_3.png]]

![[40node_7edge_2.png]]

![[40node_7edge_1.png]]



## Problem 2

