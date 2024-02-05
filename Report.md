<div align="center">
<h1> CT421 Assignment 1 </h1>
<h2> Leo Chui, Aoife Mulligan </h2>
<h3><a href="https://www.github.com/czz592/ct421-assignment/">GitHub Repo</a></h3>
</div>

# Part A

## Representation

We decided to use strings to represent the problem and solutions, as it was the most natural representation when considering the problem landscape as described by the assignment brief, and proved to be the easiest to understand.

## Fitness Function

### 1.1 OneMax Problem

The fitness is based on the number of 1's in the solution / individual. The more 1 that is present in the bitstring, the higher the fitness, which is negated to produce a negative score.

### 1.2 Target String

Like section [1.1](report.md#1.1%20onemax%20problem), except the last 5 digits are replaced with 0. A target string is instantiated, and for every matching character in the solution string, the fitness is increased. The score is negated before returning for consistency.

### 1.3 Deceptive Landscape

The fitness function first checks if there are any 1 present in the string.

If 1 is present in the string, the function iterates over all characters of the string, and adds 1 to a score variable, which will be negated before being returned. 

However, if there are no 1 present, a.k.a. there are only 0 present in the string, the score is 2*len(bitstring).

This promotes more 1's in the bitstring, despite max score being 60 in our case.

## Selection

The selection mechanism that is implemented is tournament selection. 

A $k$ (defaults to 3) number of individuals are selected at random from the population, and their fitnesses are compared, before returning the individual with the highest fitness.

## Crossover

The crossover mechanism that is implemented is one point crossover.

The function applies crossover probablistically to each pair of the parents to create children from those parents. Data past the crossover point (determined at random) is copied into the child, and the process is inverted for the other child.

## Mutation

The mutation function loops through the string and swaps the bit at $i$th position if the random float is lower than the mutate_rate, which defaults to 1/STRING_SIZE, which defaults to 30.

## Elitism

The elitism function calculates the number of individuals to select as elites, which is determined by the ELITE_FACTOR. The function then sorts the population based on the fitness score, and selects the top number of individuals and returns them.

## Plots



## Results

The algorithm converged quickly for all sections of part A, including 1.3 Deceptive landscape.

## Contribution Details

Discussion of best representation, what operations to use on solutions, and basic structure of GA. Coding was done in various ways, such as using Visual Studio Code's Live Share extension (Co-author section in commit messages were removed), paired programming (in-person and virtual), and synced files through GitHub. 

### Aoife Mulligan (20307646)

For this project I began by creating an initial, basic genetic algorithm. It didn't really work too well, so I went and did some research to understand it more. I realised that I wasn't fully understanding the crossover and mutation parts. Leo and I worked together to build the mutation parts then. 

### Leo Chui (20343266)

- Refined various components of GA.
- Layout of the report and basic descriptions.

---

# Part B

## Representation

Our method of representing the bin packing problem is as follows.

- An individual, or a solution, is a list of bins.
- Each bin is represented as a string consisting of 1's and 0's.
- Each bin is of length $n$, the number of items.
- 1 means that the item at the index is in the bin, and vice versa.

This method of representation is extremely similar to the representation of part A, and this meant that most of the code from part A were still applicable, with the only difference being the additional dimension, which can be easily compensated for.

## Selection

The selection method we used is tournament selection, code for which we took from part A.

## Crossover

Not implemented yet.

## Mutation

The concept of mutation is the same as part A, except with the addtional dimension, mutation now operates within the individual, on each of its bins.

## Elitism

Elitism is the same code from part A.

## Plots

### No Heuristics or constraints



## Results

### No Heuristics or constraints

- Poor performance, does not converge
- 

## Contribution Details

- Similar to part A
- Lengthy discussion regarding representation and implementation of code

### Aoife Mulligan (20307646)



### Leo Chui (20343266)


