from pulp import *
from ingredient_list import INGREDIENTS
from smoothie_optimizer import create_model, add_constraints, solve, get_solution_data, scale_to_serving_size


def main():
    #create model into prob and ingredient_vars
    prob, ingredient_vars = create_model()
    #get choices of what to minimize for and what to constrain
    choices = get_choices()
    #adds constraints to prob
    prob = add_constraints(prob, ingredient_vars, choices)
    #solve prob
    solve(prob)
    #put solution information into a dictionary
    solutions = get_solution_data(prob, ingredient_vars)
    #print out solution information
    scaled_solutions = scale_to_serving_size(solutions, 500)
    display_results(scaled_solutions, choices)

def display_results(solutions, choices):
    
    if solutions["status"] == 1:  # 1 means 'Optimal'
        # 3. Print the results

        print("Solution found!")
        print("==================================")
        print("For your smoothie, the following measurements will meet the requirements in the cheapest way.")
        for ing in solutions["ingredients"]:
            print(f"{ing}: {solutions['ingredients'][ing]:.2f} grams")


        # 4. Print the objective value (minimum cost or calories)
        if choices["optimize_choice"] == "cost":
            print(f"Total cost of one smoothie: ${solutions["total_cost_or_calories"]:.2f}")
        elif choices["optimize_choice"] == "calories":
            print(f"Total calories of one smoothie: {solutions["total_cost_or_calories"]:.0f}")
    else:
        print("No solution found - check your constraints")

def get_choices():
    #initialize choices dictionary
    choices_dict = {}

    #determine whether to optimize for minimal cost or minimal calories
    while True:
        optimize_choice = input("Enter 1 to optimize for cost or 2 to optimize for calories:")
        if optimize_choice == "1":
            optimize_choice == "cost"
            choices_dict["optimize_choice"] = "cost"
            break
        elif optimize_choice == "2":
            optimize_choice = "calories"
            choices_dict["optimize_choice"] = "calories"
            break
        print("Please enter 1 or 2.")

    #get input for either max calories or max cost
    while True:
        try:
            if choices_dict["optimize_choice"] == "cost":
                print("The average smoothie is around 300-400 calories.")
                max_calories = float(input("Enter the maximum calories you would prefer:"))
                if max_calories > 0:
                    choices_dict["max_cost_or_calories"] = max_calories/500
                    break
            elif choices_dict["optimize_choice"] == "calories":
                print("Average smoothie cost is roughly $5")
                max_cost = float(input("Enter the maximum cost you would prefer: $"))
                if max_cost > 0:
                    choices_dict["max_cost_or_calories"] = max_cost/500
                    break
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

    #get input for minimum protein
    while True:
        try:
            print("A standard, non-protein focused smoothie has around 10 grams of protein.")
            min_protein = float(input("Enter the minimum protein you would like in grams:"))
            if min_protein > 0:
                choices_dict["min_protein"] = min_protein/500
                break
        except ValueError:
            print("Please enter a valid number")
    


    return choices_dict


if __name__ == "__main__":
    main()