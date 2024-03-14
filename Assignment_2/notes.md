Just a file that contains misc. notes and TODOs and thoughts. It's a minddump, really.

Leo:
    - each node contain list of colours, each corresponding to their neighbours, and share this list with their neighbours?
    - Python, OOP approach (interface for agents? and implement different kinds of agents - active vs lazy nodes, a.k.a. more or less willing to change)
    - possible idea for part 2:
        - Does the order in which nodes change colour or get coloured matter to the end result we can reach? a.k.a. does it make a difference if they change at random, change the most connected first, or change the least connected first?
        - something about nodes communicating with each other 
          - assertive - aggressive, but also can tell others to change
          - aggressive - changes before others do
          - passive - does whatever others tell it
          - question - assertive on aggressive? aggressive on aggressive? etc

Aoife:
    - know how many colours you have as 'minimum'
    - Each node can know themselves and their neighbours colours, and how many colours are available.
    - They cannot know the exact colour of nodes further than their neighbour, i.e. global number of potential colours
    - Implement a graph with 4 nodes - write a function to colour it with minimum two colours
    - Implement a small world graph
    - Fitness on overall graph because to the best of their knowledge (neighbours) and ability (colours available), the individual agent has coloured the graph correctly.
    - Fitness function - error of number of conflicts/constraints. Count constraints and give it a score
    - Each node is an agent - each node takes parameters: neighbours, colours. For each neighbour n, they can select a colour c
