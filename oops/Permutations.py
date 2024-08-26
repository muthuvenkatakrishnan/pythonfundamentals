def permutation(lst):
    # If the list is empty or has exactly one element then return the list as it is the
    # only permutaion possible

    if len(lst) <=1:
        return [lst]

    # An empty list to hold the permutations
    result = []

    for i in range (len(lst)):
        current = lst[i]

        remaining = lst[:i] + lst[i+1:]

        for p in permutation(remaining):
            result.append([current] + p)
    return result

lst = [1,2,3]
res = permutation(lst)
print(res)


for i in range  (1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and j!=k and i != k):
                print(f"{i}{j}{k}")