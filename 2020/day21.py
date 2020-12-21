from shared import *

def parseAllergens(line):
    contains = line[line.find('(')+10:len(line)-1]
    allergens = contains.split(', ')
    return allergens

def parseIngredients(line):
    ingredients = line[0:line.find(' (')]
    return ingredients.split(' ')

# Part A
def solveA():
    foodList = split_lines('day21.input')
    allergenSet = set()
    ingredientSet = set()

    for line in foodList:
        for a in parseAllergens(line):
            allergenSet.add(a)
        for i in parseIngredients(line):
            ingredientSet.add(i)

    suspects = dict()
    for allergen in allergenSet:
        suspects[allergen] = []
        for ingredient in ingredientSet:
            suspects[allergen].append(ingredient)

    for line in foodList:
        allergens = parseAllergens(line)
        ingredients = parseIngredients(line)

        ingredientsNotShown = list(ingredientSet)
        # Get list of ingredients that do not show up on this line.
        for i in ingredients:
            ingredientsNotShown.remove(i)

        # The allergens listed cannot be any of the ingredients not shown.
        for a in allergens:
            for i in ingredientsNotShown:
                if i in suspects[a]:
                    suspects[a].remove(i)

    # For allergens that are pinned down to one ingredient, perform process of elimination.
    safeIngredients = list(ingredientSet)
    for i in range(len(allergenSet)):
        for a in allergenSet:
            if len(suspects[a]) == 1:
                ingredient = suspects[a][0]
                if ingredient in safeIngredients:
                    safeIngredients.remove(ingredient)
                for b in allergenSet:
                    if b != a:
                        if ingredient in suspects[b]:
                            suspects[b].remove(ingredient)
           
    answer = 0
    for line in foodList:
        ingredients = parseIngredients(line)
        for i in safeIngredients:
            answer += ingredients.count(i)
    return answer

# Part B: Basically a copy-paste of Part A, but we consume one of the intermediate outputs differently.
def solveB():
    foodList = split_lines('day21.input')
    allergenSet = set()
    ingredientSet = set()

    for line in foodList:
        for a in parseAllergens(line):
            allergenSet.add(a)
        for i in parseIngredients(line):
            ingredientSet.add(i)

    suspects = dict()
    for allergen in allergenSet:
        suspects[allergen] = []
        for ingredient in ingredientSet:
            suspects[allergen].append(ingredient)

    for line in foodList:
        allergens = parseAllergens(line)
        ingredients = parseIngredients(line)

        ingredientsNotShown = list(ingredientSet)
        # Get list of ingredients that do not show up on this line.
        for i in ingredients:
            ingredientsNotShown.remove(i)

        # The allergens listed cannot be any of the ingredients not shown.
        for a in allergens:
            for i in ingredientsNotShown:
                if i in suspects[a]:
                    suspects[a].remove(i)

    # For allergens that are pinned down to one ingredient, perform process of elimination.
    safeIngredients = list(ingredientSet)
    for i in range(len(allergenSet)):
        for a in allergenSet:
            if len(suspects[a]) == 1:
                ingredient = suspects[a][0]
                if ingredient in safeIngredients:
                    safeIngredients.remove(ingredient)
                for b in allergenSet:
                    if b != a:
                        if ingredient in suspects[b]:
                            suspects[b].remove(ingredient)

    sortedAllergens = sorted(list(suspects.keys()))
    canonicalDangerousIngredients = []
    for a in sortedAllergens:
        canonicalDangerousIngredients.append(suspects[a][0])
    return ','.join(canonicalDangerousIngredients)
