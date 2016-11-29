# Zombit Pandemic

# NOTE: I spent a lot of time in my "Intro to Java" college
# class working out this problem.

# To solve it, I played around for hours with the probability
# of achieving different trees and Googled (haha) a lot. (I
# would LOVE to show you my incredibly convoluted notebook...)
# The code starts by initializing several functions: a few
# basic ones for factorial, gcd, multinomial, and partitions.
# The multinomial function takes advantage of a generalized
# binomial coefficient function (basically by expanding the
# dimension of pascal's triangle). I could have created my own
# partitions function, but I used an absolutely fascinating one
# from the web (source provided) for the sake of time.
# Since as the number of zombits grew, the number of possible
# trees grew more complex, I had to discover a way to
# efficiently calculate it. I memoized a recursive function
# which calculates the number of trees through elimination
# and with the help of the base cases, which are based on the
# form (n - 1) ** n. This was possible because I realized that
# (n - 1) ** n represented the MAXIMUM number of possible
# trees. That meant by building my way up to larger numbers, I
# wouldn't have to explain the complexity probabalistically,
# but instead just derive it by subtracting what was already
# known of previous partitions' possible trees from the max
# possible trees. I do believe that this could be written on
# one line of code, as a simple mathemtical function, but that
# would require more time and understanding of the nature of
# the complexity of the problem.

# ANOTHER NOTE: I realize that I could have simply imported
# some of the functions that I did (i.e. gcd and factorial),
# but I wanted more flexibility in memoizing. Plus, there is a
# minor sense of satisfaction and liberation when your code is
# not dependent on any major external libraries :p. Oh, that
# darn jQuery!

# Variable Key:
# partitions: set of all possible partitions not containing 1
#             or n. i.e. "[[2, 2, 2], [2, 4], [3, 3]]"
# partition: a single partition of a set i.e. "[2, 2, 3]"
# group: a single number within a parition i.e. "2"
# partial: part of a sum that is eventually calculated
# tree: a possible grouping/chain of zombits as a result of
#       their uniform random two direction selection

# Thank you for this problem!

factorials_m = {}
treeCounts_m = {2:1, 3:8} # base cases
partitions_m = {}

def factorial(n):
    if n not in factorials_m:
        product = 1
        #print range(2, n + 1)
        for number in range(2, n + 1):
            product *= number
        factorials_m[n] = product
    return factorials_m[n]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multinomial(partition):
    n = 0
    for group in partition:
        n += group
    numerator = factorial(n)
    denominator = 1
    for group in partition:
        denominator *= factorial(group)
    for group in list(set(partition)):
        k = partition.count(group)
        denominator *= factorial(k)
    return numerator / denominator

# MOST EFFICIENT PARTITION GENERATOR
# source: http://jeromekelleher.net/
def rule_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        # yields a generator:
        yield a[:k + 1]
# END PARTITION GENERATOR

def findPartitions(n):
    if n not in partitions_m:
        output = []
        # uses the generator to produce partitions:
        for x in rule_asc(n):
            if 1 not in x and n not in x:
                output.append(x)
        partitions_m[n] = output
    return partitions_m[n]

def countTrees(n):
    if n not in treeCounts_m:
        partitions = findPartitions(n)
        # max number of trees:
        total = (n - 1) ** n
        for partition in partitions:
            multiplier = multinomial(partition)
            for group in partition:
                # the recursive bit:
                multiplier *= countTrees(group)
            total -= multiplier
        treeCounts_m[n] = total
    return treeCounts_m[n]

def answer(n):
    # there is some repetition here because I had to
    # leave the countTrees function to act recursively
    partitions = findPartitions(n)
    trees = countTrees(n)
    # initial numerator:
    numerator = trees * n
    # denominator = max possible trees for n zombits
    denominator = (n - 1) ** n
    for partition in partitions:
        multiplier = multinomial(partition)
        # takes the largest partition:
        partial = partition[-1] * multiplier
        for group in partition:
            partial *= countTrees(group)
        numerator += partial
    divisor = gcd(numerator, denominator)
    # formulate the string:
    return str(numerator / divisor) + "/" + str(denominator / divisor)
