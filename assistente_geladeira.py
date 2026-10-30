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


recipies = [
    ("omelete", {"ovo", "tomate", "pimentão"}),
    ("salada", {"alface", "tomate", "pimentão", "cebola"}),
    ("cafe", {"cafe"})
]

user_name = input("Digite seu nome: ").capitalize().strip()
while (len(user_name) <= 1 or any(caractere.isdigit() for caractere in user_name)):
    user_name = input("Nome com caracteres inferiores Digite seu nome: ")
    
print("GELY, sua Assistente de Geladeira Inteligente")
print()

while True:
    menu_options = input(
        f"O que deseja hoje, {user_name}?\n"
        "1 - Adicionar uma nova receita\n"
        "2 - Procurar receitas\n"
        "3 - Visualizar receitas\n"
        "4 - Sair\n"
        ": "
    ).strip()
    match menu_options:
        case "1":
            while True:
                add_recipe_name = input("Digite o nome da receita que deseja criar.\nPara sair, digite 'Q'\n: ").strip()
                if add_recipe_name.lower() in "q":
                    break

                if not add_recipe_name or (len(add_recipe_name) <= 3 or any(caractere.isdigit() for caractere in add_recipe_name)):
                    print("Nome inválido ou muito pequeno")
        
        case "2":
            break
        
        case "3":
            break
        
        case "4":
            break
        
        case _:
            print("Opção não encontrada.\n")