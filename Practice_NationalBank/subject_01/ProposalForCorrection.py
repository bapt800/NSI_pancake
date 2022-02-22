# Ex 1

def recherche(caractere: str, mot: str):
    occur: int = 0
    for caractereOfMot in mot:
        if caractereOfMot == caractere:
            occur += 1
    return occur


assert recherche('e', "sciences") == 2
assert recherche('i', "mississippi") == 4
assert recherche('a', "mississippi") == 0


# Ex 2
pieces = [100, 50, 20, 10, 5, 2, 1]


def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else:
        return rendu_glouton(arendre, solution, i+1)

print(rendu_glouton(68, [], 0))
assert rendu_glouton(68, [], 0) == [50, 10, 5, 2, 1]
assert rendu_glouton(291, [], 0) == [100, 100, 50, 20, 20, 1]
