# smoothie_optimizer.py
from pulp import *
# ingredient data
from ingredient_list import INGREDIENTS

def create_model():
    prob = LpProblem("Smoothie_Optimization", LpMinimize)

    #creating variables for amount of each ingredient by ratio
    ingredient_vars = LpVariable.dicts("Ingredients", INGREDIENTS.keys(), lowBound=0.05, upBound=.3)
    return prob, ingredient_vars

def add_constraints(prob, ingredient_vars, choices):

    #objective function to minimize for either cost or calories based on choices dict
    if choices["optimize_choice"] == "cost":
        prob += lpSum([ingredient_vars[ing.name] * ing.cost for ing in INGREDIENTS.values()])
    elif choices["optimize_choice"] == "calories":
        prob += lpSum([ingredient_vars[ing.name] * ing.calories for ing in INGREDIENTS.values()])

    #constraint so that ratios add to 1
    prob += lpSum(ingredient_vars.values()) == 1

    #calories constraint for cost minimization
    if choices["optimize_choice"] == "cost":
        MAX_CALORIES_PER_GRAM = choices["max_cost_or_calories"]
        prob += lpSum([ingredient_vars[ing.name] * ing.calories for ing in INGREDIENTS.values()]) <= MAX_CALORIES_PER_GRAM
    
    #cost constraint for calories minization
    elif choices["optimize_choice"] == "calories":
        MAX_COST_PER_GRAM = choices["max_cost_or_calories"]
        prob += lpSum([ingredient_vars[ing.name] * ing.cost for ing in INGREDIENTS.values()]) <= MAX_COST_PER_GRAM

    #constraint that protein is over a certrain amount
    MIN_PROTEIN_PER_GRAM = choices["min_protein"]
    prob += lpSum([ingredient_vars[ing.name] * ing.protein for ing in INGREDIENTS.values()]) >= MIN_PROTEIN_PER_GRAM

    #constraint for minimum fruit content
    MIN_TOTAL_FRUIT_CONTENT = .4
    prob += lpSum([ingredient_vars[ing] for ing in ["strawberry", "banana", "blueberry"]]) >= MIN_TOTAL_FRUIT_CONTENT

    #constraint for maximum DAIRY content
    MAX_DAIRY_CONTENT = .3
    prob += (ingredient_vars["milk"] + ingredient_vars["yogurt"]) <= MAX_DAIRY_CONTENT

    return prob


def solve(prob):
    prob.solve()

def get_solution_data(prob, ingredient_vars):
    return {
        'status': prob.status,
        'ingredients': {name: value(var) for name, var in ingredient_vars.items()},
        'total_cost_or_calories': value(prob.objective)
    }

def scale_to_serving_size(solution, serving_size):
    scaled_solution = solution.copy()
    for ing in scaled_solution['ingredients']:
        solution['ingredients'][ing] *= serving_size
    scaled_solution['total_cost_or_calories'] *= serving_size
    return scaled_solution
