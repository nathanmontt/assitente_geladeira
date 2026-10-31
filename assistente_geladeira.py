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


recipe_name = ()
recipe_ingredients = {}
all_recipies = [
    # ("omelete", {"ovo", "tomate", "pimentão"}),
    # ("salada", {"alface", "tomate", "pimentão", "cebola"}),
    # ("cafe", {"cafe"})
]

user_name = input("Digite seu nome: ").capitalize().strip()
while (len(user_name) <= 1 or any(caractere.isdigit() for caractere in user_name)):
    user_name = input("Nome com caracteres inferiores Digite seu nome: ")
    
print("GELY, sua Assistente de Geladeira Inteligente")
print()

while True:
    menu_options = input(
        f"O que deseja, {user_name}?\n"
        "1 - Adicionar uma nova receita\n"
        "2 - Procurar receitas\n"
        "3 - Visualizar receitas\n"
        "4 - Sair\n"
        ": "
    ).strip()
    match menu_options:
        case "1":
            while True:
                recipe_name = input("Digite o nome da receita que deseja criar.\nPara sair, digite 'Q'\n: ").strip()

                if recipe_name.lower() in "q":
                    break

                # verificando se há nome ou se há números no meio das palavras
                while not recipe_name or (len(recipe_name) <= 2 or any(caractere.isdigit() for caractere in recipe_name)):
                    recipe_name = input("Sem nome. Digite um nome válido.\nPara sair, digite 'Q'\n: ").strip()

                
                
                # recipies.append(recipe_name)
                # print(recipies)

                # print(f"Receita: {recipies[0]}")
                # print("Ingredientes:")

                # for each_recipe_name in recipies:
                #     print(f"- {each_recipe_name}")
                # nome da receita adicionado. colocar ingredientes

                
        
        case "2":
            break
        
        case "3":
            break
        
        case "4":
            break
        
        case _:
            print("Opção não encontrada.\n")