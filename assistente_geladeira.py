# all_recipies = [
#     ("omelete", {"arroz", "carne", "miojo"}),
#     ("omelete duplo", {"arroz", "feijão", "banana", "pessego"}),
#     ("cafe", {"cafe"})
# ]

# # print(all_recipies)
# # print(all_recipies[1])
# # print(all_recipies[1][2])

# recipe = all_recipies[0]
# print(f"recipes = {recipe}")

# # recipe = all_recipies[1]
# # print(f"recipes = {recipe}")

# # recipe = all_recipies[2]
# # print(f"recipes = {recipe}")
# # print()

# print(f"Receita: {recipe[0]}")
# print("Ingredientes:")

# for ingredient in recipe[1]:
#     print(f"- {ingredient}")


# # mostrando o que o usuário tem na geladeira
# # todas as receitas


# # cada receita



print("assistente de geladeira")

while True:
    menu_options = input("opções").strip()
    match menu_options:
        case "1":
            break
        
        case _:
            print("Opção não encontrada.\n")