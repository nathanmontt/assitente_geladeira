all_recipies = [
    ("omelete", {"arroz", "feijão", "banana"}),
    ("omelete", {"arroz", "feijão", "banana", "pessego"}),
]

# print(all_recipies)
# print(all_recipies[1])
# print(all_recipies[1][2])

recipe = all_recipies
print(recipe)

print(f"Receita: {recipe[0]}")
print("Ingredientes:")

for ingredient in recipe[1]:
    print(f"- {ingredient}")