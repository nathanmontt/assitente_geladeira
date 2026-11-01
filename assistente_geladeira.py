recipe_TUPLE = ()
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
        "2 - Visualizar receitas\n"
        "3 - Sair\n"
        ": "
    ).strip()

    match menu_options:
        case "1":
            while True:
                # criando um set vazio para guardar os ingredientes
                recipe_ingredients = set()

                # pedindo o nome da receita. ela deve estar na primeira posição da tupla
                recipe_name = input("Digite o nome da receita que deseja criar.\nPara sair, digite 'Q'\n: ").strip()
                if recipe_name.lower() in "q":
                    break

                # verificações
                while not recipe_name or (len(recipe_name) <= 2 or any(caractere.isdigit() for caractere in recipe_name)):
                    recipe_name = input("Sem nome / Nome pequeno. Digite um nome válido.\nPara sair, digite 'Q'\n: ").strip()
                    if recipe_name.lower() in "q":
                        break
                
                # adicão de ingredientes
                while True:
                    recipe_ingredient_names = input(f"Adicione ingredientes para a receita {recipe_name}.\nDigite 'S' para sair.\n: ")

                    if recipe_ingredient_names.lower() in "s":
                        break

                    while not recipe_ingredient_names or (len(recipe_ingredient_names) <= 2 or any(caractere.isdigit() for caractere in recipe_ingredient_names)):
                        recipe_ingredient_names = input("Sem nome / Nome pequeno. Digite um ingrediente válido.\nPara sair, digite 'S'\n: ").strip()

                    recipe_ingredients.add(recipe_ingredient_names)

                recipe_TUPLE = (recipe_name, recipe_ingredients)
                all_recipies.append(recipe_TUPLE)

        case "2":
            for each_recipe in all_recipies:
                recipe_name = each_recipe[0]
                recipe_ingredients = each_recipe[1]

                print(f"Receita: {recipe_name}")
                print("Ingredientes")
                count = 1

                for each_ingredient in recipe_ingredients:
                    print(f"{count} - {each_ingredient}")
                    count += 1

                print()
        
        case "3":
            break
        
        case _:
            print("Opção não encontrada.\n")