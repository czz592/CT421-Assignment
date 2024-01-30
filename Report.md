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

Like section [1.1](report.md#11-onemax-problem), except the last 5 digits are replaced with 0. A target string is instantiated, and for every matching character in the solution string, the fitness is increased. The score is negated before returning for consistency.

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



## Contribution Details

- Mixed effort using VSCode's Live Share extension
- 

# Part B

