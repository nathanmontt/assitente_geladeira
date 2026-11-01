from pathlib                    import Path
from math                       import ceil
from reportlab.pdfgen           import canvas
from reportlab.lib.pagesizes    import A4
from reportlab.lib.utils        import ImageReader
from time                       import sleep

def generate_recipe_pdf(recipes):
    if not recipes:
        print("Nenhuma receita cadastrada.")
        return

    file_name = input("Digite o nome do arquivo PDF: ").strip()

    if not file_name:
        file_name = "receitas"

    if not file_name.lower().endswith(".pdf"):
        file_name += ".pdf"

    pdf = canvas.Canvas(file_name, pagesize=A4)
    page_width, page_height = A4

    # Capa
    cover_path = Path(__file__).parent / "img" / "main.png"

    if cover_path.exists():
        image = ImageReader(str(cover_path))
        image_width, image_height = image.getSize()

        scale = min(
            page_width / image_width,
            page_height / image_height
        )

        draw_width = image_width * scale
        draw_height = image_height * scale

        position_x = (page_width - draw_width) / 2
        position_y = (page_height - draw_height) / 2

        pdf.drawImage(
            image,
            position_x,
            position_y,
            width=draw_width,
            height=draw_height
        )
    else:
        pdf.setFont("Helvetica-Bold", 24)
        pdf.drawCentredString(
            page_width / 2,
            page_height / 2,
            "RECEITAS"
        )

    pdf.showPage()

    # Uma página para cada receita
    for recipe_name, ingredients in recipes:
        pdf.setFont("Helvetica-Bold", 22)
        pdf.drawCentredString(
            page_width / 2,
            780,
            recipe_name.title()
        )

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(60, 735, "Ingredientes:")

        ingredients = sorted(ingredients)

        lines_per_column = 30
        columns = max(1, ceil(len(ingredients) / lines_per_column))
        column_width = 500 / columns

        pdf.setFont("Helvetica", 12)

        for position, ingredient in enumerate(ingredients):
            column = position // lines_per_column
            line = position % lines_per_column

            position_x = 60 + column * column_width
            position_y = 705 - line * 20

            pdf.drawString(
                position_x,
                position_y,
                f"{position + 1}. {ingredient}"
            )

        pdf.showPage()

    print("Salvando arquivo", end="")
    for i in range(3):
        sleep(.6)
        print(".", end="")
    print()

    pdf.save()
    print(f"PDF criado: {file_name}")

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
        "3 - Gerar PDF\n"
        "4 - Sair\n"
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

                    recipe_ingredients.add(recipe_ingredient_names.capitalize())

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
            generate_recipe_pdf(all_recipies)

        case "4":
            break
        
        case _:
            print("Opção não encontrada.\n")