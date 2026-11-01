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
        "2 - Procurar receitas\n"
        "3 - Visualizar receitas\n"
        "4 - Sair\n"
        ": "
    ).strip()

    match menu_options:
        case "1":
            while True:
                recipe_ingredients = set()

                recipe_name = input("Digite o nome da receita que deseja criar.\nPara sair, digite 'Q'\n: ").strip()
                if recipe_name.lower() in "q":
                    break

                # verificando se há nome ou se há números no meio das palavras
                while not recipe_name or (len(recipe_name) <= 2 or any(caractere.isdigit() for caractere in recipe_name)):
                    recipe_name = input("Sem nome / Nome pequeno. Digite um nome válido.\nPara sair, digite 'Q'\n: ").strip()
                
                # como a tupla é imutavel:
                #   pra adicionar os ingredientes, preciso transformar a tupla em LISTA (nome da receita)
                #   transformar o set em LISTA (ingredientes)
                #   dar join nos 2 acima dentro do recipe
                #   voltar ao original
                #   pronto

                # só assim consigo colocar ele dentro da 
                # recipe_name_LIST = list(recipe_TUPLE)
                # recipe_name_LIST.append(recipe_TUPLE)
                # recipe_TUPLE = tuple(recipe_name_LIST)

                
                # adicão de ingredientes
                while True:
                    recipe_ingredient_names = input(f"Adicione ingredientes para a receita {recipe_name}.\nDigite 'S' para sair.\n: ")

                    if recipe_ingredient_names.lower() in "s":
                        break

                    while not recipe_ingredient_names or (len(recipe_ingredient_names) <= 2 or any(caractere.isdigit() for caractere in recipe_ingredient_names)):
                        recipe_ingredient_names = input("Sem nome / Nome pequeno. Digite um ingrediente válido.\nPara sair, digite 'S'\n: ").strip()

                    recipe_ingredients.add(recipe_ingredient_names)

                
                # print(f"Receita: {recipies[0]}")
                # print("Ingredientes:")

                # for each_recipe_TUPLE in recipies:
                #     print(f"- {each_recipe_TUPLE}")
                # nome da receita adicionado. colocar ingredientes

                
        
        case "2":
            break
        
        case "3":
            break
        
        case "4":
            break
        
        case _:
            print("Opção não encontrada.\n")