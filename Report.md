
<div align="center">

<h1> CT421 Assignment 1 </h1>

<h2> Leo Chui, Aoife Mulligan </h2>

<h3><a href="https://www.github.com/czz592/ct421-assignment/">GitHub Repo</a></h3>

</div>

# Part A

## Representation

We decided to use strings to represent the problem and solutions, as it was the most natural representation when considering the problem landscape as described by the assignment brief, and proved to be the easiest to understand. It made sense to both of us that a binary string would represent an individual for the One-max problem, and that the 1's and 0's would represent its genes.

## Fitness Functions:

### 1.1 OneMax Problem

The fitness is based on the number of 1's in the solution / individual. The more 1 that are present in the bitstring, the higher the fitness, which is negated to produce a negative score. This means that we are aiming towards finding the lowest fitness score.

### 1.2 Target String

Like section [1.1](report.md#1.1%20onemax%20problem), except the last 5 digits are replaced with 0. A target string is instantiated, and for every matching character in the solution string, the fitness is increased. A closer match with the target string will yield a better fitness. The score is negated before returning for consistency. 

### 1.3 Deceptive Landscape

The fitness function first checks if there are any 1 present in the string.

If 1 is present in the string, the function iterates over all characters of the string, and adds 1 to a score variable, which will be negated before being returned.

However, if there are no 1 present, a.k.a. there are only 0 present in the string, the score is $2* \text{len(bitstring)}$.

This promotes more 1's in the bitstring, despite max score being 60 in our case.

Our population begins as a randomly generated string of the expected length (30). It is highly unlikely that a string of all 0's will be randomly generated - therefore, our algorithm is extremely unlikely to find the most optimum solution. If it does not, by chance, find all zeros in the first generation, it will '*climb up the wrong hill*', i.e., our fitness function will promote solutions with more 1's, but once it reaches all 1's, it will still not be 'optimum' and will never find the best solution.

## Selection

The selection mechanism that is implemented is tournament selection.

A $k$ (defaults to 3) number of individuals are selected at random from the population, and their fitness's are compared, before returning the individual with the highest fitness.

## Crossover

The crossover mechanism that is implemented is one point crossover.

The function applies crossover probabilistically to each pair of the parents to create children from those parents. Data past the crossover point (determined at random) is copied into the child, and the process is inverted for the other child.

This function returns two children to be added to the next generation.

## Mutation

The mutation function loops through the string and swaps the bit at $i$ th position if the random float is lower than the mutate_rate, which defaults to 1/STRING_SIZE, which defaults to 30.

I.e., Each bit has a 3.333% chance of mutating/being flipped.

## Elitism

The elitism function calculates the number of individuals to select as elites, which is determined by the ``ELITE_FACTOR``. The function then sorts the population based on the fitness score, and selects the top number of individuals and returns them.

The ``ELITE_FACTOR`` is 1/10.

## Plots

### 1.1 OneMax



### 1.2 Target String



### 1.3 Deceptive Landscape



## Results

For all sections of part A, the algorithm converges quite quickly (usually within 200 generations), and the reproducibility of the results are high. This indicates landscapes that are not difficult in nature, even the [Deceptive Landscape](Report.md#1.3%20Deceptive%20Landscape). And this can be easily understood, given the simple nature of the problems.

That is true, except for the last problem. Due to the intentionally deceptive fitness function, a.k.a. promoting the appearance of 1's in the solution, the true optimal solution will most likely never be found.

---

# Part B

## Representation

Our method of representing the bin packing problem is as follows:

- An individual, or a solution, is a list of bins.
	- A matrix - it is a list of lists of bitstrings
- Each bin is represented as a string consisting of 1's and 0's (a bitstring)
- Each bin is of length $n$, the number of items.
- 1 means that the item at the index is in the bin, and vice versa.

  We also have an array which stores all $n$ item weights - meaning that we can easily index the bin and the weight to find the weight of the specific item.

This method of representation is extremely similar to the representation of part A, and this meant that most of the code from part A were still applicable, with the only difference being the additional dimension, which can be easily compensated for.

## Fitness Function:
  
We calculate fitness through an error function: 

$$e = (bin\_weight - capacity)^2$$ 
If the weight of the bin is greater than the capacity, we add 1000 to the error to make it a worse solution.

TODO: add check if there are two bins with the same item

## Selection

The selection method we used is tournament selection, code for which we took from part A.

For $\text{pop\_size}$ iterations, it takes $k$ random individuals from the population and returns the index of the best of those $k$.

## Crossover

Not implemented yet.

## Mutation

The concept of mutation is the same as part A, except with the addtional dimension, mutation now operates within the individual, on each of its bins.

We allow mutation to generate invalid solutions, and give them a bad score in the fitness function.

## Elitism

Elitism is the same code from part A.

## Plots

### No Heuristics or constraints

When there are no heuristics in place, the best solution for all problem sets is simply the first solution, which is created using a Next Fit Decreasing approach in the ``generate_population`` function.

**First Problem Set**:

Individual bins: 16

Generation 0, best score = 175826.000, average fitness = 175826.000 Generation 99, best score = 175826.000, average fitness = 956670.520

![](Pasted%20image%2020240205230623.png)

**Second Problem Set**:

Individual bins: 16

Generation 0, best score = 150349.000, average fitness = 150349.000 Generation 99, best score = 150349.000, average fitness = 725225.140

![](Pasted%20image%2020240205231110.png)

**Third Problem Set**:

Individual bins: 16

Generation 0, best score = 152333.000, average fitness = 152333.000 Generation 99, best score = 152333.000, average fitness = 799432.590
![](Pasted%20image%2020240205231124.png)

**Fourth Problem Set**:

Individual bins: 16

Generation 0, best score = 135723.000, average fitness = 135723.000 Generation 99, best score = 135723.000, average fitness = 694555.970
![](Pasted%20image%2020240205230158.png)

**Fifth Problem Set**:

Individual bins: 16
Generation 0, best score = 158819.000, average fitness = 158819.000 Generation 99, best score = 158819.000, average fitness = 828061.320

![](Pasted%20image%2020240205231421.png)

## Results



### No Heuristics or constraints

- Poor performance, does not converge
- 

## Contribution Details

Brainstorming and discussion of best representation, what operations to use on solutions, and basic structure of GA. Coding collaboration was done in various ways, such as using Visual Studio Code's Live Share extension (Co-author section in commit messages were removed), paired programming (in-person and virtual), and synced files through GitHub.

### Part A

We created most of the initial algorithm in person, using Live Share, before we set up the GitHub repository.

We used https://youtu.be/4XZoVQOt-0I?si=-F8PdT-eNakF7bNT and https://youtu.be/L--IxUH4fac?si=3qAjpSG_JpQEJSCI to understand the basics of programming genetic algorithms. 

### Aoife Mulligan (20307646)

For this project I began by creating an initial, basic genetic algorithm. I was struggling to get it to function properly, so I went and did some research to understand it more. I realised that I wasn't fully understanding the crossover and mutation parts. Leo and I worked together to build the mutation and crossover parts then.

For the second part of part A, Leo and I used 

### Leo Chui (20343266)

- Refined various components of GA.
- Layout of the report and basic descriptions.

### Part B

Brainstorming and discussing most intuitive way of representing the problem landscape where both parties had equal input.