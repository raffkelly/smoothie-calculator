from ingredient import *

#all values are per gram (name, cost, calories, protein, carbs, fat)
strawberry = Ingredient("strawberry", 0.007353, .33, .007, .077, .003)
banana = Ingredient("banana", .00125, .89, .011, .23, .0033)
peanut_butter = Ingredient("peanut butter", 0.006178, 5.758, .212, 0.2424, .485)
yogurt = Ingredient("yogurt", 0.005943, .7059, 0.03529, 0.04706, 0.04118)
#acai = Ingredient("acai", 0.02353, 0.7143, 0.007143, 0.05714, .05)
blueberry = Ingredient("blueberry", 0.01015, 0.5405, 0.006757, 0.1419, 0)
milk = Ingredient("milk", 0.002820, 0.5259, 0.03236, 0.04854, 0.02023)

INGREDIENTS = {
    strawberry.name: strawberry,
    banana.name: banana,
    peanut_butter.name: peanut_butter,
    yogurt.name: yogurt,
    #acai.name: acai,
    blueberry.name: blueberry,
    milk.name: milk
}