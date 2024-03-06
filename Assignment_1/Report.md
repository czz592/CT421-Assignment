
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

![[onemax.png]]

### 1.2 Target String

![[target_string.png]]

### 1.3 Deceptive Landscape

![[deceptive.png]]

## Results

For all sections of part A, the algorithm converges quite quickly (usually within 200 generations), and the reproducibility of the results are high. This indicates landscapes that are not difficult in nature, even the [Deceptive Landscape](Report.md#1.3%20Deceptive%20Landscape). And this can be easily understood, given the simple nature of the problems.

That is true, except for the last problem. Due to the intentionally deceptive fitness function, a.k.a. promoting the appearance of 1's in the solution, the true optimal solution will most likely never be found.

##### 1.1 One-Max

![[Pasted image 20240208173630.png]]

##### 1.2 Target String

![[Pasted image 20240208173802.png]]

##### 1.3 Deceptive Landscape

![[Pasted image 20240208173848.png]]

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

## Fitness Function
  
We calculate fitness through an error function: 

$$e = (bin\_weight - capacity)^2$$
	If the weight of the bin is greater than the capacity, we add 1000 to the error to make it a worse solution.
	If there are item clashes between bins of an individual, or if there is an item not present in any bin, we also add 1000 to the error.
	*Note that these are added before the error is squared*.

The error is squared before being returned.

Fitness of an individual is then calculated by summing fitness of all bins, and the aim of the GA is to minimise this score.

## Selection

The selection method we used is tournament selection, code for which we took from part A.

For $\text{pop\_size}$ iterations, it takes $k$ random individuals from the population and returns the index of the best of those $k$.

Tournament selection aims to lower error.

## Crossover

The crossover we implemented is a one-point crossover, and is the same concept as part A, except that it is within an individual, similar to [[Report#Mutation|mutation]].

## Mutation

The concept of mutation is the same as part A, except with the additional dimension, mutation now operates within the individual, on each of its bins.

We allow mutation to generate invalid solutions, and give them a bad score in the fitness function.

## Elitism

Elitism is the same code from part A.

## Plots

### Non-Random Population

When there are no heuristics in place, the best solution for all problem sets is simply the first solution, which is created using a Next Fit Decreasing approach in the ``generate_population`` function.

#### Only Mutation

##### Problem Set 1

![[mut_bpp1.png]]

##### Problem Set 2

![[mut_bpp2.png]]

##### Problem Set 3

![[mut_bpp3.png]]

##### Problem Set 4

![[mut_bpp4.png]]

##### Problem Set 5

![[mut_bpp5.png]]

#### Mutation and Crossover

##### Problem Set 1

![[mut_cross_bpp1.png]]

##### Problem Set 2

![[mut_cross_bpp2.png]]

##### Problem Set 3

![[mut_cross_bpp3.png]]

##### Problem Set 4

![[mut_cross_bpp4.png]]

##### Problem Set 5

![[mut_cross_bpp5.png]]

### Random Population

Individuals of the population are generated at random. The ``generate_population_random`` function assigns items at random with no consideration for capacity or clashes.

The best solution is typically achieved after a number of generations. Average error typically starts at a high number, before plateauing at a lower value. However, the error is still typically an astronomical value.

This seems, to us, to be due to the fact that in the ``generate_population_random`` function, while we prevent the initial bins from exceeding the capacity, we do not have any method of preventing a single item from being in two or more bins, or for avoiding situations where an item is not in any bin.
	We instead, made helper functions ``check_clashes`` and ``check_items_present`` to include in the fitness function, in the hopes that these solutions would be removed over time. 
	While they all improve quite significantly, they do not come close to the best fitness from before. 

##### Problem Set 1


![[Pasted image 20240208202720.png]]

##### Problem Set 2

![[Pasted image 20240208202841.png]]

##### Problem Set 3

![[Pasted image 20240208202914.png]]
##### Problem Set 4

![[Pasted image 20240208202930.png]]

##### Problem Set 5

![[Pasted image 20240208202946.png]]

## Results

### Non-Random Population

The non-random population showed little ability to improve over time. It had no stable sense of direction, and seemed to be generating a good score in one generation, but throwing it away and dropping in fitness score for the next generation. The data tells us that our initial grouping of the items into bins was the best score throughout. This tells us that our algorithm really struggled to make meaningful mutations and crossovers throughout this process.

We questioned whether the method of representing the problem made it difficult to produce meaningful/useful mutations, or if our initial population generation was too 'ordered' and whether it might be useful to organise it differently.

Running this, the minimum number of bins was 16. This is not a terrible solution, but the error/fitness score was in six digits, meaning that there was room for improvement, although our algorithm could not find it.

### Random Population

We tried to overcome some of the difficulties by adding a random population in the beginning - this was accompanied by stricter checking of whether or not a solution was valid. For the random population, we tried not to be overly strict with the initial population, to give a chance for a 'good' combination to appear in an order it might otherwise not be able to. We only added the constraint that the initial population must be within the correct capacity.

This run of the algorithm managed to fit the first set into 9 bins, the second set into 11 bins, the third set into 11 bins, the fourth set into 10 bins, and the fifth set into 10 bins. 

However, as mentioned previously, the error was 8 digits long for each, indicating that our 'solutions' were not optimum or valid.

#### Only Mutation

- Poor performance, converges on local optima. Fitness measured in increments of $1_e7$.

#### Mutation and Crossover

- Poor performance, converges on local optima. Fitness measured in increments of $1_e7$.

## Comments

- Representation made mutation and crossover implementations difficult to have positive effects
	- Elitism keeps individuals, and could not keep good bins
	- Mutation and crossover often resulted in invalid solutions, even though mutation operated on bin level
- Stricter constraints lead the algorithm into a more directed path, however, it is not necessarily going to lead it to a global maxima.

## Contribution Details

Brainstorming and discussion of best representation, what operations to use on solutions, and basic structure of GA. Coding collaboration was done in various ways, such as using Visual Studio Code's Live Share extension (Co-author section in commit messages were removed), paired programming (in-person and virtual), and synced files through GitHub.

### Part A

We created most of the initial algorithm in person, using Live Share, before we set up the GitHub repository.

We used https://youtu.be/4XZoVQOt-0I?si=-F8PdT-eNakF7bNT and https://youtu.be/L--IxUH4fac?si=3qAjpSG_JpQEJSCI to understand the basics of programming genetic algorithms. 

#### Aoife Mulligan (20307646)

For this project I began by creating an initial, basic genetic algorithm. I was struggling to get it to function properly, so I went and did some research to understand it more. I realised that I wasn't fully understanding the crossover and mutation parts after reading this helpful article (https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/)[Brownlee, 2021]. Leo and I worked together to build the mutation and crossover parts then.

For part A 1.2 and 1.3, Leo and I used most of our code from 1.1. We worked together using Visual Studio's LiveShare extension.

In part B I struggled a lot to initially understand the problem, which meant that I struggled to understand how to represent a solution. After a lot of discussion, Leo and I agreed to try out using a List of lists of bitstrings. I thought it would work well since we could index through an array of the weights at the same time.

When we started implementing it, we used LiveShare most of the time if we could not be in a lab together. Leo made a lot of progress on the initial code, and we managed to eventually get it working without bugs. I think we ended up representing the problem in a way that made it slightly overcomplicated, especially for Python. If I was doing this again, with the same representation, I would probably choose Java. 

Neither of us were very happy with the first results we got from the algorithm, so I thought we should change the initial population, to see if our results start improving. We worked on that together.

We also had some discussions about why our algorithms were performing the way they were, and trying to figure out what they're missing.

#### Leo Chui (20343266)

For part A, Aoife began working on the algorithm, and I helped her to develop the mutation and crossover sections, along with finishing 1.1 together using LiveShare. I set up the GitHub repository for the project after we had some code for 1.1. I also created the basic structure of the report, which Aoife then adjusted until we were both happy. For A1.2 and 1.3, the code from 1.1 was mostly reuseable.

For part B, we struggled to figure out how to properly represent the problem. Having bins and weights threw us for a while, but after some brainstorming we decided to represent each bin as a list of lists of strings, and then have a separate array of item weights to index into.

We worked a lot using LiveShare and discord calls, just trying to implement the code and get it functioning. There were quite a few issues with our code and we ended up doing a lot of debugging, sanity checks, and refactoring (as you can see in the commit messages).

Eventually, we got it up and running, but we weren't happy with how the algorithm was moving through generations - it had a lot of fluctuations. Aoife suggested changing a few things like the way we generate the population, so we did that together.

Finally, we discussed the results of our algorithms and compiled this report.
