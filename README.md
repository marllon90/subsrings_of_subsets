# Given two strings X and Y, find the max count of substring of X from subsets of Y

### First we need to create all subsets of Y:

```
def create_subsets(string):
    n = len(string)
    subsets = list()
    for i in range(0, n):
        for j in range(i, n):
            subsets.append(str(string[i:(j + 1)]))
    return subsets
```

This function get the Y string and create an array with all possible subsets, once I have all subsets of Y, I'll organize on reverse order of len, because I want to find the max count of subtring of X, in the best case I'll find in a first subset, instead of run all list of subsets:

```
    subsets = create_subsets(y)
    subsets = sorted(subsets, key=len, reverse=True)
```

## Create Candidates 

I created candidates to organize the the X string with only valid chars of subset B

```
def create_candidate(x, subset):
    candidate_chars = dict()
    for s in subset:
        if s not in candidate_chars.keys():
            candidate_chars[s] = [p for p, v in enumerate(x) if v == s]
    return candidate_chars
```

I return a dict with all unique chars of Y subset in a list of string X index positions, example:

```
x =  'abc'
subset = 'bcc'
```

The candidate_chars will be:

```
{
    'b': [1],
    'c': [2]
}
```
next example
```
x =  'abc'
subset = 'kkk'
```

The candidate_chars will be (yes, I sent an empty list of char):

```
{
    'k': []
}
```

## Validate de subtring of subset

With subsets and candidate defined, we can validade if, the subset can be created or not:

```
def validate_substring(candidate, subset):
    last_valid_position = -1
    for s in subset:
        pos = get_valid_position(candidate[s], last_valid_position)
        if len(candidate[s]) < 1:
           return -1
        if pos < 0:
            return -1
        if candidate[s][pos] > last_valid_position:
            last_valid_position = candidate[s][pos]
        else:
            return -1
    return len(subset)
```

This function validate if is possible, create a substring of X with a subset of Y, this function runs only once in each char of Y subset, verifying if the last_valid_position is minor than candidate char postion, where pos is found thru:

```
def get_valid_position(candidate, last_valid_position):
    for k, v in enumerate(candidate):
        if v > last_valid_position:
            return k
    return -1
```

If the substring can validated, we return the length of subset, else we return -1 in any different case, including the edges. Finnaly we run the subsets until we have some value different of -1 or end the loop.

```
def max_subsequence(x, y):
    subsets = create_subsets(y)
    subsets = sorted(subsets, key=len, reverse=True)
    for subset in subsets:
        candidate = create_candidate(x, subset)
        total_subset = validate_substring(candidate, subset)
        if total_subset > -1:
            return total_subset
    return 0
```

For testing solution you can call the method ```max_subsequence```, of ```solution.py``` file with the X and Y strings, as following example:

```
    max_subsequence('hackertest', 'tset')
```
