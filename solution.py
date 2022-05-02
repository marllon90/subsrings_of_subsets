def max_subsequence(x, y):
    subsets = create_subsets(y)
    subsets = sorted(subsets, key=len, reverse=True)
    for subset in subsets:
        candidate = create_candidate(x, subset)
        total_subset = validate_substring(candidate, subset)
        if total_subset > -1:
            return total_subset
    return 0

def create_subsets(string):
    n = len(string)
    subsets = list()
    for i in range(0, n):
        for j in range(i, n):
            subsets.append(str(string[i:(j + 1)]))
    return subsets

def create_candidate(x, subset):
    candidate_chars = dict()
    for s in subset:
        if s not in candidate_chars.keys():
            candidate_chars[s] = [p for p, v in enumerate(x) if v == s]
    return candidate_chars


def validate_candidate(candidate, expected_chars):
    for char in expected_chars.keys():
        if len(candidate.get(char)) < expected_chars[char]:
            return False
    return True

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

def get_valid_position(candidate, last_valid_position):
    for k, v in enumerate(candidate):
        if v > last_valid_position:
            return k
    return -1
