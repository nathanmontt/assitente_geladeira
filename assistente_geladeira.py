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

user_name = input("Digite seu nome: ").capitalize().strip()
while (len(user_name) <= 1 or any(caractere.isdigit() for caractere in user_name)):
    user_name = input("Nome com caracteres inferiores Digite seu nome: ")
    
print("GELY, sua Assistente de Geladeira Inteligente")
print()

while True:
    menu_options = input(
        f"O que deseja hoje, {user_name}?\n"
        "1 - Adicionar uma nova receita").strip()
    match menu_options:
        case "1":
            break
        
        case _:
            print("Opção não encontrada.\n")