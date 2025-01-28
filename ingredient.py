class Ingredient:
    def __init__(self, name, cost, calories, protein, carbs, fat):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        
    def ingredient_dict(self):
        ingredient_dict = {
            "name": self.name,
            "cost": self.cost,
            "calories": self.calories,
            "protein": self.protein,
            "carbs": self.carbs,
            "fat": self.fat
              }
        return ingredient_dict