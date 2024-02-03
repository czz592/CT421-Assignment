
# Current Idea

## Representation

- Individuals are lists of binary strings
- Each string represents a bin, and all strings are of length $n$, the number of items
- 0 means that the item is not in current bin, and 1 means the item is in current bin
- length of list would be Number of bins
- also have an array which stores weights
  - e.g. for bin: \[10**1**01\], we can get the italicised 1's weight by getting the weight at the 2nd index in the weights array
   

## Uncertain parts

- To determine whether or not an item can be put into a bin, a function can be used
  - Function would be an approximation algorithm, such as Best Fit Decreasing
  - This would be the population generation function (I guess?)

- Not sure how to maintain constraint on individuals after crossover and/or mutation
  - A repair function most likely needs to be introduced 
  - Or implement a constraint check (how tho???)
  - Allow (discourage / punish via fitness function)
  
Constraint and repair function may introduce bias towards a local optima instead of global depending on the problem landscape and degree of uncertainty?

Discourage / punish solutions that violates the bin capacity constraint is a more general method that does not make assumptions of problem landscape

### Recommended Testing bits

- Change algorithm so that it can take a repair function, and compare performance with non-repair counterpart


### Miscellaneous bits

- Lower bound or higher bound bins? how could they be used for the fitness function? current fitness function calculates the ratio between solution_num_bins and optimal bins (lower bound)
- Less heuristics could be a way to look at it
- Try to implement it 

### Aoife's Notes

Mutation swapping seems like the only way to do mutation - as in, the nature of the problem means we can't mutate without swapping.
E.G. if n = 4 and two of our bins are: \[1100\] and \[0011\], we want to mutate only one chromosome. The first chromosome gets selected, so we flip the bit. Then we would have \[0100\] and \[0011\], but now the first item is not in a bin. We either must create an extra bin to place the first item (which seems crazy but I guess we could try), or we flip the corresponding bit in bin 2, so that the item is now in the other bin.

The only difference between this basic example and our implementation is that our implementation will have many bins, and so when we want to swap a bit, we should randomly select the bin for it to be swapped to.

# swap with another item
swap_i = random.randint(0, len(bin) - 1)
bin[i], bin[swap_i] = bin[swap_i], bin[i]
